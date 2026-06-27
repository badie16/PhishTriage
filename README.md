# PhishTriage

PhishTriage simulates the detection phase of a Security Operations workflow — building the analytical skills needed to recognize social engineering attacks, deconstruct malicious infrastructure, and respond with precision.

[![Samples](https://img.shields.io/badge/samples-12-blue)](/samples/)
[![Analyses](https://img.shields.io/badge/analyses-12-green)](/analyses/)
[![Checklist](https://img.shields.io/badge/checklist-✔-orange)](/checklists/)

---

## Concepts Covered

- **Phishing taxonomy:** Mass Phishing, Spear Phishing, Whaling
- **Multi-channel vectors:** Email, SMS (Smishing), Voice (Vishing), QR Codes (Quishing), Search Engine Phishing
- **Domain spoofing techniques:** Typosquatting, Homoglyph attacks, Combosquatting, Subdomain traps, Dangling DNS takeover
- **Email header manipulation:** Display name spoofing, SPF/DKIM/DMARC abuse
- **Cognitive triggers:** Authority, Urgency, Curiosity, Fear/Greed
- **Advanced threats:** BitB (Browser-in-the-Browser), MFA Fatigue, TOAD (Callback Phishing), Deepfake voice/video
- **Triage protocol:** Pause → Verify → Report

---

## Structure

```
PhishTriage/
│
├── README.md
├── annonce.md
│
├── samples/          # 12 simulated phishing samples
│   ├── _index.md
│   ├── 01-email-bancaire.md
│   ├── 02-spear-ceo.md
│   ├── 03-whaling-rh.md
│   ├── 04-smishing-dhl.md
│   ├── 05-vishing-it.md
│   ├── 06-quishing-m365.md
│   ├── 07-typosquatting.md
│   ├── 08-homoglyph.md
│   ├── 09-bitb-sso.md
│   ├── 10-mfa-fatigue.md
│   ├── 11-toad-callback.md
│   └── 12-seo-poisoning.md
│
├── analyses/         # 12 detailed analysis reports
│   ├── _index.md
│   └── 01-*.md ... 12-*.md
│
├── checklists/       # Triage SOP & decision tree
│   ├── _index.md
│   ├── triage-sop.md
│   └── decision-tree.md
│
├── scripts/          # Analysis helper tools
│   ├── _index.md
│   └── ...
│
└── assets/           # Diagrams and resources
    └── _index.md
```

---

## Analyses

| # | Sample | Vector | Technique | Verdict |
|---|--------|--------|-----------|---------|
| 1 | [Email bancaire](samples/01-email-bancaire.md) | Email | Mass Phishing — Bank alert | 🔴 Malicious |
| 2 | [Spear CEO](samples/02-spear-ceo.md) | Email | BEC — CEO fraud | 🔴 Malicious |
| 3 | [Whaling RH](samples/03-whaling-rh.md) | Email | Whaling — Macro dropper | 🔴 Malicious |
| 4 | [Smishing DHL](samples/04-smishing-dhl.md) | SMS | Smishing — Package delivery | 🔴 Malicious |
| 5 | [Vishing IT](samples/05-vishing-it.md) | Voice | Vishing — RAT scam | 🔴 Malicious |
| 6 | [Quishing M365](samples/06-quishing-m365.md) | Email | Quishing — QR code login | 🔴 Malicious |
| 7 | [Typosquatting](samples/07-typosquatting.md) | Email | Typosquatting — Google clone | 🔴 Malicious |
| 8 | [Homoglyph](samples/08-homoglyph.md) | Email | Homoglyph — Cyrillic | 🔴 Malicious |
| 9 | [BitB SSO](samples/09-bitb-sso.md) | Email | BitB — Fake SSO popup | 🔴 Malicious |
| 10 | [MFA Fatigue](samples/10-mfa-fatigue.md) | Email/Push | MFA Fatigue — Push spam | 🔴 Malicious |
| 11 | [TOAD Callback](samples/11-toad-callback.md) | Email/Voice | TOAD — Callback phishing | 🔴 Malicious |
| 12 | [SEO Poisoning](samples/12-seo-poisoning.md) | Search | SEO — Fake login page | 🔴 Malicious |

---

## Triage Framework

Every analyzed message ends in one definitive action:

```
Incoming Suspicious Message
           │
    ┌──────┴──────┬──────────────┐
    ▼             ▼              ▼
  Safe        Suspicious     Malicious
    │             │              │
  Close       Warn User    Block & Escalate
```

| Verdict | Criteria |
|---------|----------|
| **Safe** | Domain matches, no urgency pressure, no sensitive data request |
| **Suspicious** | Minor domain anomaly, unusual request — needs out-of-band verification |
| **Malicious** | Confirmed spoofed domain, credential harvesting link, bypass instruction, or known IOC |

---

## Triage SOP

See [checklists/triage-sop.md](checklists/triage-sop.md) for the full Standard Operating Procedure covering:
- Email header analysis (SPF/DKIM/DMARC)
- Domain inspection (whois, typosquatting, homoglyph)
- URL decoding
- Psychological trigger detection
- Decision making

---

## Decision Tree

See [checklists/decision-tree.md](checklists/decision-tree.md) for the interactive Mermaid decision tree.

---

## Skills Demonstrated

- Threat analysis · Cyber attack awareness · Security thinking
- Email header inspection · Social engineering recognition
- IOC extraction · Triage protocol application
- Multi-vector phishing detection (email, SMS, voice, QR, search)

---

## Usage

```bash
# Browse samples
ls samples/

# Read an analysis
cat analyses/01-email-bancaire.md

# Use the triage checklist
cat checklists/triage-sop.md

# Follow the decision tree
cat checklists/decision-tree.md
```

---

## Resources

- [Google Phishing Quiz](https://phishingquiz.withgoogle.com/)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [PhishTank — Open phishing database](https://phishtank.org/)
- [CISA Phishing Guidance](https://www.cisa.gov/phishing)

---

## Author

**Badie Bahida**
- GitHub: [github.com/Badie16](https://github.com/Badie16)
- LinkedIn: [linkedin.com/in/badie-bahida](https://linkedin.com/in/badie-bahida)
