#!/usr/bin/env python3
"""Pattern/metadata scan of staged public files and all reachable Git history.

SPDX-License-Identifier: MIT
Copyright (c) 2026 @ykbballer91
Reports locations and categories, never matched credential values.
This is a scoped safety check, not a universal guarantee of secret absence.
"""
import argparse
import json
from pathlib import Path
import re
import subprocess

PATTERNS = {
    'private_key': r'-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----',
    'github_credential': r'\b(?:gh[pousr]_[A-Za-z0-9]{25,}|github_pat_[A-Za-z0-9_]{30,})\b',
    'openai_credential': r'\bsk-(?:proj-)?[A-Za-z0-9_-]{24,}\b',
    'aws_credential': r'\b(?:AKIA|ASIA)[0-9A-Z]{16}\b',
    'google_credential': r'\bAIza[0-9A-Za-z_-]{30,}\b',
    'slack_credential': r'\bxox[baprs]-[0-9A-Za-z-]{20,}\b',
    'jwt_like_credential': r'\beyJ[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{12,}\b',
    'credential_assignment': r'''(?i)(?:api[_-]?key|access[_-]?token|client[_-]?secret|password)\s*[=:]\s*["'][A-Za-z0-9_+/=-]{24,}["']''',
    'machine_home_path': r'/(?:Users|home)/[^\s/`"<>]+/[^\s`"<>]*',
    'machine_private_path': r'/private/(?:tmp|var)/[^\s`"<>]+',
    'windows_home': r'[A-Za-z]:\\Users\\[^\s]+',
    'private_app_link': r'(?:file|codex)://',
    'email_in_payload': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
}


def run(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument('--output', type=Path)
    ap.add_argument('--history-only', action='store_true')
    args = ap.parse_args()
    repo = args.repo.resolve()
    compiled = {name: re.compile(pattern) for name, pattern in PATTERNS.items()}
    findings = []
    files = []

    def scan(raw, location):
        try:
            text = raw.decode('utf-8')
        except UnicodeDecodeError:
            findings.append({'location': location, 'type': 'unexpected_binary_requires_review'})
            return
        for name, pattern in compiled.items():
            if pattern.search(text):
                findings.append({'location': location, 'type': name})

    if not args.history_only:
        files = [p for p in run(repo, 'ls-files', '-z').decode().split('\0') if p]
        for p in files:
            file = repo / p
            if file.is_symlink():
                findings.append({'location': p, 'type': 'symlink_requires_review'})
            elif file.is_file():
                scan(file.read_bytes(), p)
            else:
                findings.append({'location': p, 'type': 'tracked_file_missing'})
    objects = run(repo, 'rev-list', '--objects', '--all').decode().splitlines()
    blobs = 0
    for entry in objects:
        oid = entry.split(' ', 1)[0]
        kind = run(repo, 'cat-file', '-t', oid).decode().strip()
        if kind == 'blob':
            scan(run(repo, 'cat-file', 'blob', oid), 'git-blob:'+oid)
            blobs += 1
    # History metadata is also public. Only the chosen display and public noreply identity are allowed.
    metadata = run(repo, 'log', '--all', '--format=%H%x09%an%x09%ae%x09%cn%x09%ce').decode().splitlines()
    for row in metadata:
        oid, an, ae, cn, ce = row.split('\t')
        scan(run(repo, 'show', '-s', '--format=%B', oid), 'commit-message:'+oid)
        if an != '@ykbballer91' or cn != '@ykbballer91':
            findings.append({'location': 'commit:'+oid, 'type': 'unexpected_author_display'})
        if not all(re.fullmatch(r'(?:\d+\+)?ykbballer91@users\.noreply\.github\.com', value) for value in (ae, ce)):
            findings.append({'location': 'commit:'+oid, 'type': 'unexpected_commit_contact'})
    report = {
        'status': 'PASS' if not findings else 'BLOCKED',
        'scope': 'Tracked worktree plus all reachable Git blobs, commit messages and identities; pattern scan, no claim of universal detection',
        'tracked_files_scanned': len(files), 'git_blobs_scanned': blobs,
        'commits_checked': len(metadata), 'findings': findings,
        'secret_scan_findings': len([f for f in findings if 'credential' in f['type'] or f['type']=='private_key']),
        'unexpected_sensitive_path_or_identity_findings': len([f for f in findings if 'credential' not in f['type'] and f['type']!='private_key']),
    }
    if args.output:
        args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))
    raise SystemExit(bool(findings))


if __name__ == '__main__':
    main()
