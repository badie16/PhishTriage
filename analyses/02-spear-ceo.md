# Analyse 02 — Spear Phishing : Usurpation du CEO

## Référence
- **Échantillon** : `samples/02-spear-ceo.md`
- **Vecteur** : Email (Spear Phishing)
- **Source** : marc.dubois@maisoncorp-billing.com

## Analyse des en-têtes

| Champ | Valeur | Verdict |
|-------|--------|---------|
| From | "Marc Dubois — PDG" <marc.dubois@maisoncorp-billing.com> | ❌ Domaine non officiel |
| Reply-To | factures@maisoncorp-billing.com | ❌ Domaine suspect |
| SPF | neutral (domain not found) | ❌ Domaine inexistant |
| DKIM | absent | ❌ |
| DMARC | absent | ❌ |

## Red Flags Identifiés

| # | Red Flag | Explication |
|---|----------|-------------|
| 1 | **Domaine usurpé** | `maisoncorp-billing.com` ≠ `maisoncorp.fr` (domaine officiel) |
| 2 | **SPF/DKIM/DMARC absents** | Aucune authentification, domaine non trouvé |
| 3 | **Demande de virement urgente** | Le PDG ne demande jamais de virement par email sans procédure |
| 4 | **IBAN international suspect** | Compte Hong Kong (HK85) — incohérent avec un fournisseur habituel |
| 5 | **"Joignable uniquement par email"** | Impossible de vérifier par téléphone → isolement de la cible |
| 6 | **Montant élevé** | 48 750 € — seuil typique des BEC (Business Email Compromise) |
| 7 | **Absence de pièces justificatives** | Pas de devis, bon de commande, ou contrat fournisseur |

## Déclencheurs Cognitifs

- **Autorité** : Usurpation du PDG, signature imposante "Président-Directeur Général"
- **Urgence** : "URGENT", "avant 17h", "aujourd'hui"
- **Isolement** : "Je suis à l'étranger, joignable uniquement par email"

## Classification
- **Verdict** : 🔴 **Malicious**
- **Justification** : BEC (Business Email Compromise) classique — usurpation de dirigeant, virement frauduleux

## Décision de Triage
- **Action** : 🚫 **Block & Escalate**
- **Procédure** : Contacter le PDG par téléphone (hors bande), prévenir le SOC, bloquer le virement si déjà initié

## IOCs Extracted

| Type | Valeur |
|------|--------|
| Domaine | maisoncorp-billing.com |
| Email | marc.dubois@maisoncorp-billing.com |
| Email | factures@maisoncorp-billing.com |
| IBAN | HK85 1234 5678 9012 3456 |
| Bénéficiaire | Shenzhen Electronics Ltd |
| Montant | 48 750 € |
