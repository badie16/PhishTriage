# Carte de Référence Rapide — Triage Phishing

## 1. Header Check (30s)

```
From        → Domaine officiel ?
Reply-To    = From ?
Return-Path = From ?
SPF         = pass ?
DKIM        = pass ?
DMARC       = pass ?
```

**Si un ≠ → 🔴 Malicious**

## 2. Domain Check

```
TLD sûr ? (.com/.fr/.org) ou suspect ? (.tk/.top/.xyz)
Âge > 6 mois ?
Lettres normales ou homoglyphes/unicode ?
```

## 3. Psychological Triggers

| Trigger | Phrase |
|---------|--------|
| Urgence | "immédiatement", "sous 24h" |
| Peur | "suspendu", "piratage" |
| Autorité | "PDG", "Support", "Administrateur" |
| Curiosité | "document confidentiel" |

**≥ 2 triggers + demande d'action = danger**

## 4. Verdict

| Couleur | Action |
|---------|--------|
| 🟢 Safe | Close |
| 🟡 Suspicious | Warn User + hors-bande |
| 🔴 Malicious | Block & Escalate |

## 5. Règles d'Or

1. En cas de doute → Suspicious (jamais Safe)
2. Identifiants/mot de passe/virement → 🔴 Malicious
3. .docm/.exe/.vbs/.js → 🔴 Malicious
4. Vérification hors-bande = canal DIFFÉRENT
