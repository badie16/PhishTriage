# Analyse 06 — Quishing : QR Code Microsoft 365

## Référence
- **Échantillon** : `samples/06-quishing-m365.md`
- **Vecteur** : Email avec QR code (Quishing)
- **Source** : noreply@m365-alerts.tk

## Analyse des en-têtes

| Champ | Valeur | Verdict |
|-------|--------|---------|
| From | "Microsoft 365 Security" <noreply@m365-alerts.tk> | ❌ Domaine .tk |
| Reply-To | security@m365-alerts.tk | ❌ Même domaine frauduleux |
| SPF | absent | ❌ |
| DKIM | absent | ❌ |
| DMARC | absent | ❌ |

## Red Flags Identifiés

| # | Red Flag | Explication |
|---|----------|-------------|
| 1 | **Domaine .tk** | Tokelau — domaine gratuit, massivement utilisé par les fraudeurs |
| 2 | **QR code dans un email** | Les services légitimes ne demandent jamais de scanner un QR code depuis un email |
| 3 | **"Liens désactivés pour sécurité"** | Fausse justification pour forcer l'utilisation du QR code |
| 4 | **QR code contourne les filtres** | Les scanners URL ne détectent pas le lien caché dans l'image |
| 5 | **URL de destination différente** | `microsoft-365-verify.tk` ≠ `microsoft.com` |
| 6 | **Demande de connexion** | Page usurpant Microsoft 365 pour voler identifiants |
| 7 | **Expiration à 2 heures** | Urgence artificielle |

## Déclencheurs Cognitifs

- **Autorité** : "Microsoft 365 Security"
- **Urgence** : "Expire dans 2 heures"
- **Obligation** : "Authentification requise", "Mise à jour de sécurité"

## Analyse Technique

Le QR code est un contournement des filtres de sécurité :
- Les passerelles email analysent les URL dans le corps
- Mais ne peuvent pas décoder les QR codes en amont
- L'utilisateur scanne avec son téléphone → hors du périmètre de sécurité de l'entreprise

## Classification
- **Verdict** : 🔴 **Malicious**
- **Justification** : Quishing — vol d'identifiants Microsoft 365 via QR code

## Décision de Triage
- **Action** : 🚫 **Block & Escalate**
- **Recommandation** : Bloquer le domaine, sensibiliser les utilisateurs à ne pas scanner de QR codes dans les emails

## IOCs Extracted

| Type | Valeur |
|------|--------|
| Domaine | m365-alerts.tk |
| Domaine | microsoft-365-verify.tk |
| Email | noreply@m365-alerts.tk |
| URL QR | https://microsoft-365-verify.tk/login |
