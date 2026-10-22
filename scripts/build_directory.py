#!/usr/bin/env python3
"""Validate data/projects.json and refresh the GitHub directory. No dependencies."""

import argparse
import html
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import quote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE = 'https://madewithhyperframes.com'
GROUPS = [
    ('Product demos', {'Product Demo'}),
    ('Motion and creative', {'Motion', 'Creative', 'AI'}),
    ('Explainers and education', {'Explainer', 'Education', 'Tutorial'}),
    ('3D scenes', {'3D'}),
    ('Launches and marketing', {'Marketing'}),
    ('Short films and music', {'Short Film', 'Music'}),
]
CATEGORIES = set().union(*(categories for _, categories in GROUPS))


def valid_url(value, allow_asset=False):
    if not isinstance(value, str) or not value or any(c.isspace() for c in value):
        return False
    if allow_asset and value.startswith(('/videos/', '/posters/')):
        return '..' not in value.split('/')
    parsed = urlsplit(value)
    return parsed.scheme in ('http', 'https') and bool(parsed.hostname) and not parsed.username and not parsed.password


def validate(projects):
    if not isinstance(projects, list) or not projects:
        raise ValueError('data/projects.json must contain a nonempty array.')
    seen_slugs, seen_urls = set(), set()
    for index, project in enumerate(projects, 1):
        prefix = f'Entry {index}'
        if not isinstance(project, dict):
            raise ValueError(f'{prefix}: expected an object.')
        for key in ('slug', 'title', 'creator', 'category', 'prompt', 'videoUrl', 'creatorUrl'):
            if not isinstance(project.get(key), str) or not project[key].strip():
                raise ValueError(f'{prefix}: {key} must be a nonempty string.')
        slug = project['slug']
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug) or slug in seen_slugs:
            raise ValueError(f'{prefix}: invalid or duplicate slug {slug!r}.')
        seen_slugs.add(slug)
        if project['videoUrl'] in seen_urls:
            raise ValueError(f'{slug}: duplicate original video URL.')
        seen_urls.add(project['videoUrl'])
        if project['category'] not in CATEGORIES:
            raise ValueError(f'{slug}: unknown category {project["category"]!r}.')
        stack = project.get('stack')
        if not isinstance(stack, list) or not stack or not all(isinstance(s, str) and s.strip() for s in stack):
            raise ValueError(f'{slug}: stack must contain tool names.')
        if type(project.get('prompt_partial')) is not bool:
            raise ValueError(f'{slug}: prompt_partial must be true or false.')
        if 'featured' in project and type(project['featured']) is not bool:
            raise ValueError(f'{slug}: featured must be true or false.')
        for key in ('videoUrl', 'creatorUrl', 'playbackUrl', 'thumbnailUrl'):
            if key in project and not valid_url(project[key], key in ('playbackUrl', 'thumbnailUrl')):
                raise ValueError(f'{slug}: invalid {key}.')
        if 'duration' in project and not re.fullmatch(r'\d+:[0-5]\d', str(project['duration'])):
            raise ValueError(f'{slug}: duration must use m:ss format.')
        if 'submittedAt' in project:
            if not isinstance(project['submittedAt'], str):
                raise ValueError(f'{slug}: submittedAt must be an ISO timestamp.')
            date = datetime.fromisoformat(project['submittedAt'].replace('Z', '+00:00'))
            if date.tzinfo is None:
                raise ValueError(f'{slug}: submittedAt needs a timezone.')


def escape(value):
    text = html.escape(str(value), quote=False)
    for char in ('\\', '|', '[', ']', '*', '_', '`'):
        text = text.replace(char, f'&#{ord(char)};')
    return ' '.join(text.split())


def url(value):
    return quote(value, safe=':/?#&=%+@,;~!$*-._')


def link(label, target):
    return f'[{escape(label)}]({url(target)})'


def anchor(title):
    return title.lower().replace(' ', '-')


def tools(project):
    return ' + '.join('HyperFrames' if s.lower() == 'hyperframes' else s for s in project['stack'])


def text_link(project, lines):
    label = 'Context' if project['prompt_partial'] else 'Full prompt'
    return link(label, f'data/projects.json#L{lines[project["slug"]]}')


def project_url(project):
    return f'{SITE}/projects/{project["slug"]}'


def table(rows):
    return '\n'.join('| ' + ' | '.join(row) + ' |' for row in rows)


def rank(project):
    date = project.get('submittedAt')
    timestamp = datetime.fromisoformat(date.replace('Z', '+00:00')).timestamp() if date else float('-inf')
    return (
        not any(tool.lower() == 'hyperframes' for tool in project['stack']),
        not project.get('featured', False),
        -timestamp,
        project['slug'],
    )


def gallery(projects, lines):
    # Each group shows up to three previews, prioritizing HyperFrames and featured entries.
    selected = sorted((p for p in projects if p.get('thumbnailUrl')), key=rank)[:3]
    if not selected:
        return ''
    rows = [[f'**{escape(p["title"])}**' for p in selected], ['---'] * len(selected)]
    rows.append([
        f'[![{escape(p["title"])}]({url(SITE + p["thumbnailUrl"] if p["thumbnailUrl"].startswith("/") else p["thumbnailUrl"])})]({url(project_url(p))})'
        for p in selected
    ])
    rows.append(['By ' + link(p['creator'], p['creatorUrl']) for p in selected])
    rows.append([escape(tools(p)) + (f' · {p["duration"]}' if p.get('duration') else '') for p in selected])
    rows.append([link('Watch', project_url(p)) + ' · ' + link('Original', p['videoUrl']) + ' · ' + text_link(p, lines) for p in selected])
    return table(rows)


def render(projects, lines):
    groups = [(name, [p for p in projects if p['category'] in categories]) for name, categories in GROUPS]
    groups = [(name, items) for name, items in groups if items]
    full = sum(not p['prompt_partial'] for p in projects)
    summary = f'**{len(projects)} videos** · **{full} entries marked as full prompts** · **{len(projects) - full} with context or excerpts**\n\n'
    summary += '## Browse by category\n\n'
    summary += table([
        ['Category', 'Videos', 'Full list'], ['---', '---:', '---'],
        *[[link(name, '#' + anchor(name)), str(len(items)), link('Browse', 'DIRECTORY.md#' + anchor(name))] for name, items in groups],
    ])
    showcase = []
    directory = [
        '<!-- Generated by scripts/build_directory.py from data/projects.json. -->',
        '# Video directory',
        f'All **{len(projects)} videos** in the public catalog. Browse by category or use your browser’s Find command to search titles, creators, and tools.',
        '**[Watch on Made with HyperFrames](https://madewithhyperframes.com)** · **[Back to the showcase](README.md)** · **[Submit a video](CONTRIBUTING.md)**',
        'Video titles link to the original posts. Full prompt and Context links open the corresponding text in `data/projects.json` on GitHub. Labels reflect the supplied data; context can be a summary or excerpt.',
        '## Categories\n\n' + '\n'.join(f'- {link(name, "#" + anchor(name))} ({len(items)})' for name, items in groups),
    ]
    for name, items in groups:
        showcase.append(f'## {name}\n\n{gallery(items, lines)}\n\n{link(f"Browse all {len(items)} in this category →", "DIRECTORY.md#" + anchor(name))}')
        rows = [['Video', 'Creator', 'Tools', 'Length', 'Prompt / context'], ['---', '---', '---', '---', '---']]
        for p in sorted(items, key=lambda p: (p['title'].casefold(), p['slug'])):
            rows.append([link(p['title'], p['videoUrl']), link(p['creator'], p['creatorUrl']), escape(tools(p)), p.get('duration', '—'), text_link(p, lines)])
        directory.append(f'## {name}\n\n' + table(rows))
    return summary, '\n\n'.join(showcase), '\n\n'.join(directory) + '\n'


def replace_block(readme, name, content):
    start, end = f'<!-- BEGIN {name} -->', f'<!-- END {name} -->'
    if readme.count(start) != 1 or readme.count(end) != 1 or readme.index(start) >= readme.index(end):
        raise ValueError(f'README.md needs exactly one ordered {name} marker pair.')
    before, rest = readme.split(start)
    _, after = rest.split(end)
    return before + start + '\n\n' + content.strip() + '\n\n' + end + after


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Validate data and report stale generated files without writing.')
    args = parser.parse_args()
    try:
        raw = (ROOT / 'data/projects.json').read_text(encoding='utf-8')
        projects = json.loads(raw)
        validate(projects)
        lines = {}
        current = None
        for number, line in enumerate(raw.splitlines(), 1):
            slug_match = re.match(r'\s*"slug"\s*:\s*"([a-z0-9-]+)"', line)
            if slug_match:
                current = slug_match.group(1)
            if re.match(r'\s*"prompt"\s*:', line) and current:
                lines[current] = number
        if set(lines) != {p['slug'] for p in projects}:
            raise ValueError('Format data/projects.json with one field per line and slug before prompt.')
        summary, showcase, directory = render(projects, lines)
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        readme = replace_block(readme, 'DIRECTORY SUMMARY', summary)
        readme = replace_block(readme, 'VIDEO SHOWCASE', showcase)
        outputs = {'README.md': readme, 'DIRECTORY.md': directory}
        stale = [name for name, content in outputs.items() if not (ROOT / name).exists() or (ROOT / name).read_text(encoding='utf-8') != content]
        if args.check and stale:
            print('Out of date: ' + ', '.join(stale) + '. Run python3 scripts/build_directory.py.', file=sys.stderr)
            return 1
        if not args.check:
            for name in stale:
                (ROOT / name).write_text(outputs[name], encoding='utf-8')
        print(f'Validated {len(projects)} videos. ' + ('Generated files are current.' if args.check else 'README and directory refreshed.'))
        return 0
    except (ValueError, OSError) as error:
        print(f'Error: {error}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
