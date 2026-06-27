# Analyse 04 — Smishing : Faux colis DHL

## Référence
- **Échantillon** : `samples/04-smishing-dhl.md`
- **Vecteur** : SMS (Smishing)
- **Source** : +33 6 99 88 77 66 (numéro court non officiel)

## Analyse

| Champ | Valeur | Verdict |
|-------|--------|---------|
| Expéditeur affiché | 33766 | ❌ DHL officiel utilise des numéros différents |
| URL | dhl-fr-livraison.top | ❌ Domaine .top récent |
| Âge du domaine | 2 jours | ❌ Fraîchement enregistré |

## Red Flags Identifiés

| # | Red Flag | Explication |
|---|----------|-------------|
| 1 | **Expéditeur non vérifié** | Le numéro court 33766 n'est pas répertorié par DHL France |
| 2 | **Domaine .top** | Extension bon marché, utilisée quasi-exclusivement par des fraudeurs |
| 3 | **Domaine enregistré il y a 2 jours** | Durée de vie très courte — typique des campagnes smishing |
| 4 | **Frais de douane de 2,99€** | Montant faible pour maximiser le clic sans réflexion |
| 5 | **Menace de hausse de prix** | "Passera à 12,99€ dans 24h" — pression temporelle |
| 6 | **URL non officielle** | DHL utilise `dhl.com` ou `dhl.fr`, pas `dhl-fr-livraison.top` |
| 7 | **Fautes d'orthographe** | "expedition", "impayes", "livre" — absence d'accents |

## Déclencheurs Cognitifs

- **Curiosité/Pratique** : "Votre colis est en attente"
- **Urgence** : "Passera à 12,99€ dans 24h"
- **Perte potentielle** : Pénalité financière

## Classification
- **Verdict** : 🔴 **Malicious**
- **Justification** : Smishing classique — vol d'identifiants bancaires via faux paiement de douane

## Décision de Triage
- **Action** : 🚫 **Block & Escalate**
- **Recommandation** : Transférer le SMS au 33700 (signalement spam), bloquer l'expéditeur, ne pas cliquer

## IOCs Extracted

| Type | Valeur |
|------|--------|
| Numéro | +33 6 99 88 77 66 |
| Domaine | dhl-fr-livraison.top |
| URL | https://dhl-fr-livraison.top/paiement |
| Réf expédition | DHL-FR-982341 (fausse) |
