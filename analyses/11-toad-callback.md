# Analyse 11 — TOAD : Callback Phishing

## Référence
- **Échantillon** : `samples/11-toad-callback.md`
- **Vecteur** : Email + Appel vocal (TOAD — Telephone Oriented Attack Delivery)
- **Source** : info@facturation-paypal-safe.com

## Analyse des en-têtes

| Champ | Valeur | Verdict |
|-------|--------|---------|
| From | "Service Abonnement" <info@facturation-paypal-safe.com> | ❌ Domaine suspect |
| Reply-To | support@facturation-paypal-safe.com | ❌ Domaine frauduleux |
| SPF | absent | ❌ |
| DKIM | absent | ❌ |
| DMARC | absent | ❌ |

## Red Flags Identifiés

| # | Red Flag | Explication |
|---|----------|-------------|
| 1 | **Domaine long et suspect** | `facturation-paypal-safe.com` — accumulation de mots rassurants |
| 2 | **Numéro surtaxé** | 0 891 45 67 89 — numéro non standard PayPal |
| 3 | **Absence de lien de contestation** | Pas de possibilité de contester en ligne uniquement par téléphone |
| 4 | **Montant de 549,99€** | Suffisamment élevé pour paniquer mais crédible |
| 5 | **"Service Litiges — ouvert 7j/7"** | Argument pseudo-rassurant |
| 6 | **Signature PayPal usurpée** | PayPal utilise `paypal.com`, pas un sous-domaine |
| 7 | **Pas de détail de transaction** | Pas de numéro de facture PayPal valide |

## Déclencheurs Cognitifs

- **Peur/Perte financière** : "549,99€ débités"
- **Curiosité/Colère** : "Si vous n'avez pas effectué cet achat"
- **Fausse solution** : "Appelez-nous pour le remboursement"

## Analyse Technique — TOAD

Le TOAD est en 3 phases :

**Phase 1 — Amorçage**
- Email avec fausse facture → crée un sentiment d'urgence

**Phase 2 — Appel**
- La cible appelle le numéro → tombe sur un faux conseiller
- Le fraudeur demande les identifiants bancaires "pour le remboursement"
- Ou demande d'installer un logiciel de prise en main à distance (AnyDesk, TeamViewer)

**Phase 3 — Exploitation**
- Vol de compte bancaire
- Ou installation de ransomware

## Classification
- **Verdict** : 🔴 **Malicious**
- **Justification** : TOAD — Callback phishing avec vol d'identifiants bancaires

## Décision de Triage
- **Action** : 🚫 **Block & Escalate**
- **Procédure** : 
  1. Ne pas appeler le numéro
  2. Vérifier son compte PayPal directement (site officiel)
  3. Signaler l'email et le numéro
  4. Ne jamais donner d'identifiants par téléphone

## IOCs Extracted

| Type | Valeur |
|------|--------|
| Domaine | facturation-paypal-safe.com |
| Email | info@facturation-paypal-safe.com |
| Email | support@facturation-paypal-safe.com |
| Numéro | 0 891 45 67 89 (surtaxé) |
| FAUX ref | INV-2026-7843 |
| FAUX montant | 549,99€ |
