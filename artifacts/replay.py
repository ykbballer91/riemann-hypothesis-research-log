#!/usr/bin/env python3
# STATUS: RIEMANN HYPOTHESIS OPEN
# Public export utility by @ykbballer91; AI-assisted.
# SPDX-License-Identifier: MIT
"""Reconstruct an isolated source layout before explicitly running one saved script.

This utility is not a certificate verifier and does not validate historical claims.
It never downloads third-party papers/code or runs preservation validators.
"""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile

PUBLIC_ROOT = Path(__file__).resolve().parents[1]
MANIFEST = PUBLIC_ROOT / "data/source-manifest.json"
BLOCKED_LIMITS = {
    "REQUIRES_EXCLUDED_THIRD_PARTY_ANCILLARY_CODE",
    "REQUIRES_EXCLUDED_THIRD_PARTY_TEX_SOURCE",
    "HISTORICAL_REPOSITORY_AND_PRESERVATION_VALIDATOR_NOT_PORTABLE",
    "HISTORICAL_METADATA_GENERATOR_NOT_A_MATHEMATICAL_CHECK",
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--list", action="store_true", help="List scripts and declared limitations; execute nothing")
    parser.add_argument("--script", help="Original relative source path of one selected Python script")
    parser.add_argument("--workspace", type=Path, help="New or empty directory outside this public repository; default is a new temporary directory")
    parser.add_argument("--prepare-only", action="store_true", help="Reconstruct files but do not run the script")
    parser.add_argument("arguments", nargs=argparse.REMAINDER, help="Arguments after -- are passed verbatim to the saved script")
    options = parser.parse_args()
    manifest = json.loads(MANIFEST.read_text())
    records = manifest["entries"]
    scripts = {row["source_path"]: row for row in records if row["source_path"].endswith(".py")}
    if options.list:
        for source, row in sorted(scripts.items()):
            limits = row.get("code_portability", {}).get("known_limits", [])
            print(source + ("  [" + "; ".join(limits) + "]" if limits else "  [not rerun; external packages may be required]"))
        return 0
    if options.script not in scripts:
        parser.error("Choose one source path shown by --list. No arbitrary command is accepted.")
    limits = scripts[options.script].get("code_portability", {}).get("known_limits", [])
    if BLOCKED_LIMITS.intersection(limits) and not options.prepare_only:
        parser.error("This script is not independently runnable from the curated export: " + "; ".join(limits) + ". Use --prepare-only to inspect its historical context.")
    if options.workspace:
        workspace = options.workspace.expanduser().resolve()
        if workspace == PUBLIC_ROOT or PUBLIC_ROOT in workspace.parents:
            parser.error("Workspace must be outside the public repository to protect saved records.")
        if workspace.is_symlink():
            parser.error("Workspace must not be a symlink.")
        if workspace.exists() and (not workspace.is_dir() or any(workspace.iterdir())):
            parser.error("Workspace must be new or empty; existing data is never overwritten.")
        workspace.mkdir(parents=True, exist_ok=True)
    else:
        workspace = Path(tempfile.mkdtemp(prefix="rh-public-replay-")).resolve()
    for row in records:
        public_path = (PUBLIC_ROOT / row["public_path"]).resolve()
        target = (workspace / row["source_path"]).resolve()
        if PUBLIC_ROOT not in public_path.parents or workspace not in target.parents:
            raise RuntimeError("Invalid path in manifest")
        payload = public_path.read_bytes()
        if hashlib.sha256(payload).hexdigest() != row["export_sha256"]:
            raise RuntimeError("Public payload hash mismatch: " + row["public_path"])
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(payload)
    print("Prepared isolated workspace:", workspace, flush=True)
    print("Historical result files are copied for context. Any new output belongs to this workspace, not the archived certification.", flush=True)
    if options.prepare_only:
        return 0
    passed = options.arguments[1:] if options.arguments[:1] == ["--"] else options.arguments
    print("Running saved research code with the current Python; dependencies are not installed automatically.", flush=True)
    return subprocess.run([sys.executable, str(workspace/options.script), *passed], cwd=workspace).returncode


if __name__ == "__main__":
    raise SystemExit(main())
