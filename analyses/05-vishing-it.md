# Analyse 05 — Vishing : Appel support IT

## Référence
- **Échantillon** : `samples/05-vishing-it.md`
- **Vecteur** : Appel vocal (Vishing)
- **Source** : +33 1 88 45 23 01 (VoIP, Caller ID spoofé)

## Analyse

| Champ | Valeur | Verdict |
|-------|--------|---------|
| Caller ID affiché | Microsoft Support | ❌ Spoofé |
| Numéro réel | +33 1 88 45 23 01 | ⚠️ VoIP jetable |
| URL demandée | bit.ly/ms-secure-remote | ❌ Lien raccourci |

## Red Flags Identifiés

| # | Red Flag | Explication |
|---|----------|-------------|
| 1 | **Caller ID usurpé** | "Microsoft Support" peut être affiché arbitrairement en VoIP |
| 2 | **Microsoft ne contacte jamais les utilisateurs** | Aucun FAI ou éditeur ne téléphone pour des "intrusions" |
| 3 | **Urgence extrême** | "7 minutes avant chiffrement" — pression temporelle maximale |
| 4 | **Demande d'action immédiate** | "Ouvrez Chrome et tapez ce lien" — prise de contrôle à distance |
| 5 | **Lien raccourci** | bit.ly masque la destination réelle |
| 6 | **Terminologie vague** | "Ransomware", "connexions vers Biélorussie" — détails techniques inexacts |
| 7 | **Intimidation** | "Vous voulez perdre toutes vos données ?" — manipulation émotionnelle |
| 8 | **Aucun identifiant employé** | Pas de nom, pas de numéro de ticket, pas d'email de confirmation |

## Déclencheurs Cognitifs

- **Peur** : "Intrusion", "ransomware", "perdre toutes vos données"
- **Urgence** : "7 minutes", "tout de suite"
- **Autorité** : "Support Microsoft", ton technique

## Classification
- **Verdict** : 🔴 **Malicious**
- **Justification** : Vishing avec tentative de prise de contrôle à distance (RAT/support scam)

## Décision de Triage
- **Action** : 🚫 **Block & Escalate**
- **Procédure** : Raccrocher, ne pas rappeler, signaler au SI de l'entreprise, informer les collègues

## IOCs Extracted

| Type | Valeur |
|------|--------|
| Numéro | +33 1 88 45 23 01 |
| URL court | bit.ly/ms-secure-remote |
| Société usurpée | Microsoft |
| Nom employé | "Thomas" (faux) |
