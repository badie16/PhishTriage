# Analyse 01 — Fausse alerte de sécurité bancaire

## Référence
- **Échantillon** : `samples/01-email-bancaire.md`
- **Vecteur** : Email (Mass Phishing)
- **Source** : no-reply@securite-banque-nationale.xyz

## Analyse des en-têtes

| Champ | Valeur | Verdict |
|-------|--------|---------|
| From | "Sécurité Banque Nationale" <no-reply@securite-banque-nationale.xyz> | ❌ Domaine inconnu |
| Reply-To | fraud@phisher.io | ❌ Domaine différent du From |
| Return-Path | bounce@phisher.io | ❌ Domaine différent |
| SPF | fail | ❌ Non autorisé |
| DKIM | présent mais domaine = phisher.io | ❌ Domaine non lié à la banque |
| DMARC | fail (quarantine) | ❌ Échoué |

## Red Flags Identifiés

| # | Red Flag | Explication |
|---|----------|-------------|
| 1 | **Domaine usurpé** | `securite-banque-nationale.xyz` → la banque nationale utilise `.fr` ou `.com`, pas `.xyz` |
| 2 | **Reply-To différent** | Les emails légitimes ont un Reply-To cohérent avec le domaine From |
| 3 | **SPF/DKIM/DMARC en échec** | L'expéditeur n'est pas autorisé à utiliser le domaine de la banque |
| 4 | **Urgence artificielle** | "Sous 24 heures votre compte sera suspendu" → précipitation |
| 5 | **Demande d'action sensible** | Clic sur un lien pour "confirmer son identité" |
| 6 | **Adresse IP suspecte** | IP 185.220.101.23 mentionnée (connue pour activités malveillantes) |
| 7 | **Piège grammatical** | "dans les plus brefs délais" — formule administrative excessive |
| 8 | **URL trompeuse** | Le sous-domaine `securite-banque-nationale.xyz/verify/identite` imite une page officielle |

## Déclencheurs Cognitifs

- **Urgence** : "sous 24 heures", "compte suspendu"
- **Peur** : "connexion suspecte depuis la Russie"

## Classification
- **Verdict** : 🔴 **Malicious**
- **Justification** : SPF/DKIM/DMARC échoués, domaine frauduleux, hameçonnage d'identifiants bancaires confirmé

## Décision de Triage
- **Action** : 🚫 **Block & Escalate**
- **Destinataire** : SOC / Équipe sécurité

## IOCs Extracted

| Type | Valeur |
|------|--------|
| Domaine | securite-banque-nationale.xyz |
| Domaine | phisher.io |
| Email | no-reply@securite-banque-nationale.xyz |
| Email | fraud@phisher.io |
| IP | 185.220.101.23 |
| URL | https://securite-banque-nationale.xyz/verify/identite |
