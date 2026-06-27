#!/usr/bin/env python3
"""
URL Analyzer — Inspect suspicious URLs for phishing indicators.

Usage:
    python url-analyzer.py <url>
    python url-analyzer.py -f urls.txt
"""

import sys
import json
import argparse
from urllib.parse import urlparse
from datetime import datetime


def analyze_url(url: str) -> dict:
    parsed = urlparse(url)
    domain = parsed.netloc.lower()
    path = parsed.path
    query = parsed.query

    red_flags = []
    suspicious_tlds = {'.tk', '.ml', '.ga', '.cf', '.top', '.xyz',
                       '.club', '.work', '.gq', '.pw', '.cc'}

    # Extract TLD
    tld = None
    for stld in suspicious_tlds:
        if domain.endswith(stld):
            tld = stld
            break
    if not tld and '.' in domain:
        tld = '.' + domain.rsplit('.', 1)[-1]

    # Check 1: Suspicious TLD
    if tld in suspicious_tlds:
        red_flags.append(f"Extension suspecte : {tld}")

    # Check 2: IP address in hostname
    import re
    if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', domain):
        red_flags.append("Adresse IP utilisée au lieu d'un nom de domaine")

    # Check 3: Too many subdomains
    parts = domain.split('.')
    if len(parts) > 3:
        red_flags.append(f"Nombre anormal de sous-domaines ({len(parts)})")

    # Check 4: Homoglyph detection (non-ASCII)
    for char in domain:
        if ord(char) > 127:
            red_flags.append(f"Caractère non-ASCII détecté : {char} (U+{ord(char):04X})")
            break

    # Check 5: Typosquatting patterns
    known_domains = ['google', 'g00gle', 'paypal', 'paypa1', 'microsoft',
                     'micr0soft', 'amazon', 'amaz0n', 'facebook', 'faceb00k',
                     'apple', 'app1e', 'netflix', 'netfl1x']
    for kd in known_domains:
        if kd in domain:
            red_flags.append(f"Domaine connu imité : motif '{kd}' détecté")

    # Check 6: @ symbol in URL (credential smuggling)
    if '@' in url:
        red_flags.append("Symbole @ dans l'URL — tentative de smuggling")

    # Check 7: excessive path depth
    depth = len([p for p in path.split('/') if p])
    if depth > 5:
        red_flags.append(f"Chemin anormalement profond ({depth} niveaux)")

    # Check 8: suspicious keywords in path
    suspicious_keywords = ['login', 'signin', 'verify', 'secure', 'confirm',
                           'update', 'validate', 'authenticate', 'steal']
    path_lower = path.lower()
    for kw in suspicious_keywords:
        if kw in path_lower:
            red_flags.append(f"Mot-clé suspect dans le chemin : '{kw}'")

    score = len(red_flags)

    if score == 0:
        verdict = "🟢 Aucun indicateur détecté"
    elif score <= 2:
        verdict = "🟡 Suspect — vérification recommandée"
    else:
        verdict = "🔴 Malicieux — ne pas ouvrir"

    return {
        'url': url,
        'domain': domain,
        'tld': tld,
        'path': path,
        'score': score,
        'red_flags': red_flags,
        'verdict': verdict,
        'analysis_date': datetime.now().isoformat(),
    }


def main():
    parser = argparse.ArgumentParser(description='Analyze URLs for phishing indicators')
    parser.add_argument('url', nargs='?', help='URL to analyze')
    parser.add_argument('-f', '--file', help='File containing URLs (one per line)')
    parser.add_argument('-j', '--json', action='store_true', help='Output as JSON')
    args = parser.parse_args()

    urls = []
    if args.url:
        urls.append(args.url)
    if args.file:
        with open(args.file) as f:
            urls.extend(line.strip() for line in f if line.strip())

    if not urls:
        parser.print_help()
        sys.exit(1)

    results = []
    for url in urls:
        result = analyze_url(url)
        results.append(result)

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        for r in results:
            print(f"\n{'='*60}")
            print(f"URL     : {r['url']}")
            print(f"Domaine : {r['domain']}")
            print(f"TLD     : {r['tld']}")
            print(f"Score   : {r['score']} / {len(r['red_flags'])} indicateurs")
            print(f"Verdict : {r['verdict']}")
            if r['red_flags']:
                print(f"Drapeaux :")
                for flag in r['red_flags']:
                    print(f"  ⚠️  {flag}")


if __name__ == '__main__':
    main()
