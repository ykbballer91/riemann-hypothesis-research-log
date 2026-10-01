"""Canonical bilingual editorial routes. Copyright 2026 @ykbballer91. MIT."""
from pathlib import Path

SITE_URL = 'https://ykbballer91.github.io/riemann-hypothesis-research-log'
LANGUAGES = ('ja', 'en')
SLUGS = {'home': '', 'index': 'guide', 'source-map': 'sources'}
NAV = {
 'ja': [('ホーム','home'),('読み方','index'),('現在地','current-state'),('履歴','timeline'),('ロードマップ','roadmap'),('出典','source-map')],
 'en': [('Home','home'),('Guide','index'),('Current state','current-state'),('Timeline','timeline'),('Roadmap','roadmap'),('Sources','source-map')],
}

def editorial_info(relative):
    p=Path(relative)
    if len(p.parts)>=3 and p.parts[0]=='docs' and p.parts[1] in LANGUAGES and p.suffix=='.md':
        return p.parts[1], Path(*p.parts[2:]).with_suffix('').as_posix()
    return None

def route(lang, key):
    slug=SLUGS.get(key,key)
    return Path(lang)/slug/'index.html'

def url_for(destination):
    p=Path(destination).as_posix()
    if p.endswith('index.html'):p=p[:-10]
    return SITE_URL+'/'+p

def source_for(lang,key):
    return Path('docs')/lang/(key+'.md')

def legacy_info(relative):
    p=Path(relative)
    if p==Path('README.md'):return 'en','home'
    if p==Path('README.ja.md'):return 'ja','home'
    if p.parts and p.parts[0]=='docs' and p.suffix=='.md' and not editorial_info(p):
        key=Path(*p.parts[1:]).with_suffix('').as_posix()
        return ('ja' if key.startswith('updates/') else 'en'),key
    return None
