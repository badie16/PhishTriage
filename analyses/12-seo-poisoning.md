# Analyse 12 — SEO Poisoning : Faux site de login

## Référence
- **Échantillon** : `samples/12-seo-poisoning.md`
- **Vecteur** : Moteur de recherche (SEO Poisoning)
- **Source** : Aucun email — recherche Google "Canva login"

## Analyse

| Champ | Valeur | Verdict |
|-------|--------|---------|
| Moteur | Google | ⚠️ Annonce sponsorisée |
| URL affichée | canva-login.top | ❌ Domaine frauduleux |
| Âge domaine | 4 jours | ❌ Très récent |
| Certificat | Let's Encrypt | ⚠️ Valide mais pas de garantie |

## Red Flags Identifiés

| # | Red Flag | Explication |
|---|----------|-------------|
| 1 | **Domaine .top** | Extension bon marché et peu fiable |
| 2 | **Domaine enregistré il y a 4 jours** | Durée de vie extrêmement courte |
| 3 | **Annonce Google Ads malveillante** | L'attaquant paie pour apparaître en haut des résultats |
| 4 | **Page de login clonée** | Copie exacte de la page Canva officielle |
| 5 | **Formulaire POST externe** | Les identifiants sont envoyés au serveur de l'attaquant |
| 6 | **Contenu SEO bidon** | Pages générées automatiquement pour le référencement |
| 7 | **Pas de meta noindex** | Le site est volontairement indexé dans Google |

## Déclencheurs Cognitifs

- **Confiance dans Google** : "C'est en haut des résultats, c'est forcément le bon site"
- **Habitude** : L'utilisateur tape "Canva login" par réflexe
- **Design familier** : Page identique → pas de suspicion

## Analyse Technique — SEO Poisoning

1. L'attaquant crée un site cloné de Canva
2. Génère 10+ pages de contenu SEO (articles, tutoriels) avec backlinks
3. Achète des publicités Google Ads pointant vers le site
4. Le site remonte dans les résultats (payants + organiques)
5. L'utilisateur clique, entre ses identifiants → volés

**Variante** : Attaque "sponsored results" — les annonces Google Ads sont en tête des résultats et passent souvent inaperçues comme pubs.

## Classification
- **Verdict** : 🔴 **Malicious**
- **Justification** : SEO Poisoning / Publicité malveillante — vol d'identifiants

## Décision de Triage
- **Action** : 🚫 **Block & Escalate**
- **Recommandation** : 
  1. Vérifier l'URL dans la barre d'adresse AVANT de taper son mot de passe
  2. Signaler l'annonce à Google (Google Ads Fraud)
  3. Changer immédiatement son mot de passe si déjà saisi
  4. Activer la MFA

## IOCs Extracted

| Type | Valeur |
|------|--------|
| Domaine | canva-login.top |
| URL | https://www.canva-login.top/ |
| Script | /steal-credentials.php |
| Certificat | Let's Encrypt |
| Date enregistrement | 2026-06-23 (approximatif) |
| Moteur | Google Ads / SEO |
