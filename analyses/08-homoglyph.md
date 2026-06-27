# Analyse 08 — Homoglyph : Substitution cyrillique

## Référence
- **Échantillon** : `samples/08-homoglyph.md`
- **Vecteur** : Email (Homoglyph Attack)
- **Source** : support@аmаzon-security.com

## Analyse des en-têtes

| Champ | Valeur | Verdict |
|-------|--------|---------|
| From | "Amazon Support" <support@аmаzon-security.com> | ❌ Domaine homoglyphe |
| Domaine en ASCII | xn--mazn-security-3zbh.com | ❌ Encodage PunyCode |
| SPF | probablement absent | ❌ |
| DKIM | absent | ❌ |
| DMARC | absent | ❌ |

## Red Flags Identifiés

| # | Red Flag | Explication |
|---|----------|-------------|
| 1 | **Caractères cyrilliques** | `а` (U+0430) remplace `a` (U+0061) — visuellement identique |
| 2 | **Domaine PunyCode** | `xn--mazn-security-3zbh.com` trahit la présence d'Unicode non-ASCII |
| 3 | **Scénario crédible** | Commande Apple MacBook à 1 249,99€ — montant plausible |
| 4 | **Données personnelles** | Mention de l'adresse et des 4 derniers chiffres de la CB → voleurs d'identité |
| 5 | **Bouton d'annulation** | CTA pousse à cliquer pour "annuler" une commande inexistante |
| 6 | **Absence de numéro de commande valide** | #AMZ-78421 ne suit pas le format Amazon standard |

## Déclencheurs Cognitifs

- **Peur/Perte financière** : "1 249,99€ débités"
- **Curiosité** : "Détails de la commande suspecte" avec infos personnelles
- **Confiance usurpée** : Logo Amazon et design de l'email

## Analyse Technique — Homoglyph

Les caractères cyrilliques `а` (U+0430) et `а` (U+0430) sont visuellement identiques au `a` latin :
- `аmаzon` au lieu de `amazon`
- Rendu identique dans 99% des navigateurs et clients email
- Seul l'encodage PunyCode dans la barre d'adresse permet de détecter la supercherie

## Classification
- **Verdict** : 🔴 **Malicious**
- **Justification** : Homoglyph attack — vol d'identifiants Amazon / fraude

## Décision de Triage
- **Action** : 🚫 **Block & Escalate**
- **Recommandation** : Copier l'URL et la coller dans un bloc-notes pour voir le PunyCode, signaler à Amazon

## IOCs Extracted

| Type | Valeur |
|------|--------|
| Domaine visuel | аmаzon-security.com |
| Domaine réel | xn--mazn-security-3zbh.com |
| Email | support@аmаzon-security.com |
| URL | https://www.аmаzon-security.com/annuler |
| FAUX numéro commande | AMZ-78421 |
| FAUX montant | 1 249,99€ |
