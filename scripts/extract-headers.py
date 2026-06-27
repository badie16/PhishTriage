#!/usr/bin/env python3
"""
Email Header Extractor — Parse and analyze email headers for phishing indicators.

Usage:
    paste raw email headers into stdin, or pipe from a file.
    cat email.txt | python extract-headers.py
    python extract-headers.py -f email.txt
"""

import sys
import json
import argparse
import re
from email import message_from_string
from email.policy import default


SUSPICIOUS_TLDS = {'.tk', '.ml', '.ga', '.cf', '.top', '.xyz',
                   '.club', '.work', '.gq', '.pw', '.cc'}


def extract_headers(raw_email: str) -> dict:
    msg = message_from_string(raw_email, policy=default)

    headers = {
        'from': msg.get('From', ''),
        'reply_to': msg.get('Reply-To', ''),
        'return_path': msg.get('Return-Path', ''),
        'subject': msg.get('Subject', ''),
        'to': msg.get('To', ''),
        'date': msg.get('Date', ''),
        'message_id': msg.get('Message-ID', ''),
        'received': msg.get_all('Received', []),
        'spf': '',
        'dkim': '',
        'dmarc': '',
        'authentication_results': msg.get('Authentication-Results', ''),
    }

    # Parse SPF from Authentication-Results
    auth = headers['authentication_results']
    spf_match = re.search(r'spf=(\w+)', auth, re.IGNORECASE)
    if spf_match:
        headers['spf'] = spf_match.group(1)

    dkim_match = re.search(r'dkim=(\w+)', auth, re.IGNORECASE)
    if dkim_match:
        headers['dkim'] = dkim_match.group(1)

    dmarc_match = re.search(r'dmarc=(\w+)', auth, re.IGNORECASE)
    if dmarc_match:
        headers['dmarc'] = dmarc_match.group(1)

    return headers


def analyze_headers(headers: dict) -> dict:
    findings = []
    score = 0

    def extract_domain(email_addr):
        match = re.search(r'@([\w.-]+)', email_addr)
        return match.group(1) if match else ''

    from_domain = extract_domain(headers['from'])
    reply_domain = extract_domain(headers['reply_to'])
    return_domain = extract_domain(headers['return_path'])

    # Check 1: Reply-To mismatch
    if reply_domain and from_domain and reply_domain != from_domain:
        findings.append(f"Reply-To ({reply_domain}) ≠ From ({from_domain})")
        score += 2

    # Check 2: Return-Path mismatch
    if return_domain and from_domain and return_domain != from_domain:
        findings.append(f"Return-Path ({return_domain}) ≠ From ({from_domain})")
        score += 2

    # Check 3: SPF
    spf = headers.get('spf', '')
    if spf and spf.lower() not in ('pass', ''):
        findings.append(f"SPF = {spf} (attendu: pass)")
        score += 1

    # Check 4: DKIM
    dkim = headers.get('dkim', '')
    if dkim and dkim.lower() not in ('pass', ''):
        findings.append(f"DKIM = {dkim} (attendu: pass)")
        score += 1

    # Check 5: DMARC
    dmarc = headers.get('dmarc', '')
    if dmarc and dmarc.lower() not in ('pass', ''):
        findings.append(f"DMARC = {dmarc} (attendu: pass)")
        score += 1

    # Check 6: Missing auth headers
    if not spf:
        findings.append("SPF absent")
        score += 1
    if not dkim:
        findings.append("DKIM absent")
        score += 1
    if not dmarc:
        findings.append("DMARC absent")
        score += 1

    # Check 7: Suspicious TLD in from domain
    if from_domain:
        tld = '.' + from_domain.rsplit('.', 1)[-1] if '.' in from_domain else ''
        if tld in SUSPICIOUS_TLDS:
            findings.append(f"Extension suspecte du domaine From : {tld}")
            score += 2

    # Check 8: Multiple Received hops
    received_count = len(headers.get('received', []))
    if received_count == 0:
        findings.append("Aucun header Received — possible message forgé")
        score += 1

    if score == 0:
        verdict = "🟢 En-têtes valides"
    elif score <= 3:
        verdict = "🟡 Suspect — vérifier manuellement"
    else:
        verdict = "🔴 Malicieux — ne pas faire confiance"

    return {
        'headers': headers,
        'findings': findings,
        'score': score,
        'verdict': verdict,
    }


def main():
    parser = argparse.ArgumentParser(description='Analyze email headers')
    parser.add_argument('-f', '--file', help='File containing raw email headers')
    parser.add_argument('-j', '--json', action='store_true', help='Output as JSON')
    args = parser.parse_args()

    if args.file:
        with open(args.file) as f:
            raw = f.read()
    else:
        raw = sys.stdin.read()

    if not raw.strip():
        print("Erreur : aucun header fourni", file=sys.stderr)
        sys.exit(1)

    headers = extract_headers(raw)
    result = analyze_headers(headers)

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"\n{'='*60}")
        print("📬 EN-TÊTES EXTRAITS")
        print(f"{'='*60}")
        print(f"From        : {headers['from']}")
        print(f"Reply-To    : {headers['reply_to']}")
        print(f"Return-Path : {headers['return_path']}")
        print(f"Subject     : {headers['subject']}")
        print(f"To          : {headers['to']}")
        print(f"Date        : {headers['date']}")
        print(f"SPF         : {headers['spf'] or 'absent'}")
        print(f"DKIM        : {headers['dkim'] or 'absent'}")
        print(f"DMARC       : {headers['dmarc'] or 'absent'}")

        print(f"\n{'='*60}")
        print(f"🔍 ANALYSE")
        print(f"{'='*60}")
        print(f"Score : {result['score']} indicateurs")
        print(f"Verdict : {result['verdict']}")
        if result['findings']:
            print(f"Drapeaux :")
            for f in result['findings']:
                print(f"  ⚠️  {f}")

        print(f"\nReçu via {len(headers.get('received', []))} serveur(s)")


if __name__ == '__main__':
    main()
