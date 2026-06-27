# 🎣 PhishTriage — Phishing Awareness Analysis

## 🎯 Objective

Analyze sample emails and messages to identify phishing attempts, document red flags, and apply a structured triage response.

---

## 📋 Deliverables

- Identify suspicious links and keywords in phishing messages
- List all red flags found in each analyzed sample
- Explain why the message is unsafe
- Apply the **Pause → Verify → Report** triage protocol

---

## 🧩 Key Skills

Threat analysis · Cyber attack awareness · Security thinking · Email header inspection · Social engineering recognition

---

## 📌 What You Will Build

A **Phishing Triage Toolkit** consisting of:

- **Phishing email analyses** — one detailed report per sample, covering red flags, threat classification, and triage decision
- **A non-expert triage checklist** — standard operating procedures for parsing From/Reply-To/Return-Path headers and identifying suspicious subdomains
- **A decision tree** — guiding any user from *Incoming Suspicious Message* to one of three definitive outcomes: **Safe → Close**, **Suspicious → Warn User**, or **Malicious → Block & Escalate**

---

## ⚠️ Why This Matters

- **80%** of security breaches involve phishing
- In controlled red-team simulations, **40%** of employees fall for phishing and vishing campaigns
- It takes an average of only **82 seconds** from the start of a phishing campaign for an attacker to get their first click
- The modern cybersecurity perimeter is no longer the network firewall — **it is the user**

---

## 🔍 Threat Landscape Covered

| Vector | Description |
|--------|-------------|
| Email Phishing | Spoofed sender domains, fake forwarded chains, malicious attachments |
| Smishing (SMS) | Malicious links disguised as package deliveries or bank alerts |
| Vishing (Voice) | Caller ID spoofing impersonating IT support or government agencies |
| Quishing (QR Code) | Malicious QR codes bypassing desktop URL filters |
| Search Engine Phishing | SEO poisoning placing lookalike sites above legitimate login portals |

---

## 🧠 Attack Anatomy

```
Input (The Bait)         →   Process (The Psychology)   →   Output (The Defense)
Delivery method &            Cognitive triggers that         Triage checklist,
domain spoofing              bypass logical verification     decision tree & report
```

**Cognitive triggers to recognize:**
- **Authority** — Impersonating C-suite, IT, or law enforcement
- **Urgency** — Artificial time pressure ("Account locked in 30 minutes")
- **Curiosity** — Exploiting knowledge gaps ("See what your colleague said about you")
- **Fear/Greed** — Legal threats or unexpected prize giveaways

---

## ✅ Qualification Criteria

- Complete all phishing sample analyses
- Each analysis must include: red flags identified, threat classification, and triage decision
- All deliverables verified for quality before submission
