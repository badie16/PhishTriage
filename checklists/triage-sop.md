# ✅ Triage SOP — Procédure Opérationnelle Standard

## 📋 Prérequis

Avant toute analyse, rassembler :
- Email complet avec en-têtes bruts (Show Original / Afficher le message source)
- SMS avec expéditeur complet
- URL ou QR code concerné
- Pièces jointes (NE PAS ouvrir sans analyse)

---

## 1️⃣ Pause — Observation initiale

### 1.1 Questions de premier niveau

| Question | Si Oui | Si Non |
|----------|--------|--------|
| Connaissez-vous l'expéditeur ? | Aller à 1.2 | ⚠️ Suspect |
| Attendez-vous ce message ? | Aller à 1.2 | ⚠️ Suspect |
| Le ton vous semble normal ? | Aller à 1.2 | ⚠️ Suspect |
| Y a-t-il une pièce jointe inattendue ? | ❌ Alerter | Continuer |

---

## 2️⃣ Vérification — Analyse technique

### 2.1 Analyse des en-têtes (Show Original)

Inspecter dans cet ordre :

```
From:           ⬅ L'expéditeur affiché
Reply-To:       ⬅ Où va la réponse (souvent différent en phishing)
Return-Path:    ⬅ Retour de bounce (doit correspondre au domaine From)
Message-ID:     ⬅ Format du ID (souvent suspect chez les fraudeurs)
Received:       ⬅ IP et serveurs de transit
SPF:            ⬅ L'IP est-elle autorisée à envoyer pour ce domaine ?
DKIM:           ⬅ Le message est-il signé par le domaine ?
DMARC:          ⬅ La politique DMARC est-elle respectée ?
```

**Indicateurs d'authenticité :**

| Champ | ✅ Légitime | ❌ Frauduleux |
|-------|------------|---------------|
| SPF | `pass` | `fail`, `softfail`, `neutral` |
| DKIM | `pass` (domaine = From) | `fail`, absent, domaine différent |
| DMARC | `pass` | `fail`, `quarantine`, `reject` |
| Reply-To | Même domaine que From | Domaine différent |
| Return-Path | Même domaine que From | Domaine différent |

### 2.2 Inspection du domaine

```
Étape 1 : Copier le domaine de l'expéditeur
Étape 2 : Vérifier le TLD (extension)
    ✅ .com, .fr, .org, .net (légitimes)
    ❌ .tk, .ml, .ga, .cf, .top, .xyz, .club, .work (souvent frauduleux)
Étape 3 : Vérifier l'âge du domaine (whois)
    ✅ > 1 an
    ❌ < 6 mois
Étape 4 : Détecter les substitutions visuelles
    - google.com → g00gle.com (chiffres)
    - amazon.com → аmazon.com (cyrillique)
    - microsoft.com → m1crosoft.com
Étape 5 : Rechercher le domaine officiel (comparaison)
```

### 2.3 Analyse de l'URL

```bash
# Décoder l'URL complète
# 1. Vérifier le vrai domaine (entre https:// et le premier /)
# 2. Vérifier les sous-domaines (ex: securite.banque.com.pirate.xyz)
# 3. Tester avec https://urlscan.io ou VirusTotal
# 4. NE PAS CLIQUER — survoler (hover) pour voir l'URL
```

**Tromperies courantes :**

| URL affichée | URL réelle |
|-------------|------------|
| `https://paypal.com.security.facture.xyz` | Domaine = `.xyz` |
| `https://www.googleworkspace.com@evil.com` | Domaine = `evil.com` |
| `https://amazon.com.secure.php?id=123` | Domaine = `amazon.com.secure` |

### 2.4 Analyse des pièces jointes

| Extension | Risque | Action |
|-----------|--------|--------|
| .txt, .pdf | Faible | Ouvrir avec précaution |
| .doc, .xls | Moyen | Vérifier les macros |
| .docm, .xlsm | ⚠️ Élevé | Contient des macros |
| .exe, .msi, .vbs, .js | 🔴 Très élevé | Bloquer immédiatement |
| .htm, .html | Moyen | Peut contenir du phishing |
| .zip, .rar, .7z | Moyen | Vérifier le contenu |

### 2.5 Analyse des déclencheurs psychologiques

| Déclencheur | Phrase typique |
|-------------|----------------|
| **Urgence** | "Sous 24h", "immédiatement", "dernier avertissement" |
| **Autorité** | "PDG", "Support technique", "Administrateur" |
| **Peur** | "Compte suspendu", "Activité suspecte", "Ransomware" |
| **Curiosité** | "Quelqu'un a partagé...", "Document confidentiel" |
| **Récompense** | "Vous avez gagné", "Remise exclusive", "Remboursement" |

**Règle :** Si le message contient ≥ 2 déclencheurs + une demande d'action → **Suspect**

---

## 3️⃣ Rapport — Décision de triage

### 3.1 Arbre de décision simplifié

```
Message suspect ?
├── Domaine ≠ officiel → 🔴 MALICIOUS → Block & Escalate
├── Domaine = officiel mais SPF/DKIM/DMARC fail → 🔴 MALICIOUS
├── Domaine ok mais demande sensible + urgence → 🟡 SUSPICIOUS
├── Domaine ok, pas d'urgence, demande normale → 🟢 SAFE
└── Douteux → 🟡 SUSPICIOUS → Warn User + Vérification hors bande
```

### 3.2 Actions par verdict

| Verdict | Action | Délai |
|---------|--------|-------|
| 🟢 **Safe** | Fermer (Close) | Immédiat |
| 🟡 **Suspicious** | Prévenir l'utilisateur + vérification hors bande | < 24h |
| 🔴 **Malicious** | Bloquer + Escalader au SOC | Immédiat |

### 3.3 Vérification hors bande (pour suspicieux)

Contacter l'expéditeur présumé par un **canal différent** :
- ✅ Appel téléphonique (numéro officiel, pas celui de l'email)
- ✅ Visite du site officiel (taper l'URL manuellement)
- ✅ Application mobile officielle
- ❌ NE PAS répondre à l'email
- ❌ NE PAS rappeler le numéro donné

---

## 4️⃣ Checklist rapide (30 secondes)

```
□ L'expéditeur est-il connu et attendu ?
□ Le domaine correspond-il au site officiel ?
□ SPF/DKIM/DMARC sont-ils valides ?
□ Y a-t-il une urgence artificielle ?
□ Le message demande-t-il une action sensible (clique, identifiants, virement) ?
□ Y a-t-il une pièce jointe inattendue ?
□ L'URL de destination correspond-elle au texte affiché ?
□ Y a-t-il des fautes d'orthographe ou un ton inhabituel ?
```

**Si ≥ 2 réponses "Non" ou suspectes → appliquer le triage**

---

## 5️⃣ Références rapides

| Outil | URL | Usage |
|-------|-----|-------|
| VirusTotal | https://www.virustotal.com | Analyser fichiers/URL |
| urlscan.io | https://urlscan.io | Analyse de sites |
| Whois | https://who.is | Âge du domaine |
| Google Safe Browsing | https://transparencyreport.google.com/safe-browsing/search | Réputation URL |
| Have I Been Pwned | https://haveibeenpwned.com | Fuites d'identifiants |
