# Analyse 03 — Whaling : Fausse communication RH

## Référence
- **Échantillon** : `samples/03-whaling-rh.md`
- **Vecteur** : Email avec pièce jointe malveillante (Whaling)
- **Source** : rh@groupe-hr-secure.net

## Analyse des en-têtes

| Champ | Valeur | Verdict |
|-------|--------|---------|
| From | "Ressources Humaines — Groupe" <rh@groupe-hr-secure.net> | ❌ Domaine inconnu |
| Reply-To | rh-candidature@groupe-hr-secure.net | ❌ Sous-domaine différent |
| SPF | absent | ⚠️ |
| DKIM | absent | ❌ |
| DMARC | absent | ❌ |

## Red Flags Identifiés

| # | Red Flag | Explication |
|---|----------|-------------|
| 1 | **Domaine non officiel** | `groupe-hr-secure.net` — pas le domaine RH officiel de l'entreprise |
| 2 | **Pièce jointe .docm** | Format avec macros activées — vecteur malware classique |
| 3 | **Mot de passe fourni dans l'email** | Contournement des filtres de sécurité et analyse antivirale |
| 4 | **Message non signé numériquement** | Aucune signature S/MIME ou certificat |
| 5 | **Destinataire inhabituel** | Une directrice financière ne reçoit pas de révision de contrat par email non sollicité |
| 6 | **Ton inapproprié** | "Document confidentiel" — les RH officielles utilisent des portails sécurisés |

## Déclencheurs Cognitifs

- **Curiosité** : "Révision de votre contrat", "Document confidentiel"
- **Autorité** : "Service Juridique & RH", "Groupe Holding International"
- **Confiance artificielle** : Mot de passe fourni pour "simplifier"

## Analyse Technique de la Pièce Jointe

- **Type** : `.docm` (Word avec macros)
- **Comportement attendu** : À l'ouverture, la macro télécharge et exécute un payload (Cobalt Strike / Agent Tesla / Dridex)
- **Protection** : Mot de passe fourni dans l'email pour contourner les sandbox

## Classification
- **Verdict** : 🔴 **Malicious**
- **Justification** : Whaling avec dropper macro — cible C-level, livraison de malware

## Décision de Triage
- **Action** : 🚫 **Block & Escalate**
- **Procédure** : Bloquer la PJ au niveau du gateway, analyser le hash sur VirusTotal, prévenir la cible

## IOCs Extracted

| Type | Valeur |
|------|--------|
| Domaine | groupe-hr-secure.net |
| Email | rh@groupe-hr-secure.net |
| Email | rh-candidature@groupe-hr-secure.net |
| Fichier | Contrat_Revision_Sophie_Martin.docm |
| Hash SHA256 | a4b5c6d7e8f90123456789abcdef0123456789abcdef0123456789abcdef01234 |
| Mot de passe | RH-2026-42SM |
