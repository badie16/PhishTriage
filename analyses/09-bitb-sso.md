# Analyse 09 — BitB : Browser-in-the-Browser

## Référence
- **Échantillon** : `samples/09-bitb-sso.md`
- **Vecteur** : Email (BitB — Browser-in-the-Browser)
- **Source** : security@gitlab-secure.net

## Analyse des en-têtes

| Champ | Valeur | Verdict |
|-------|--------|---------|
| From | "GitLab Security" <security@gitlab-secure.net> | ❌ Domaine non officiel |
| Reply-To | security@gitlab-secure.net | ❌ Domaine frauduleux |
| SPF | absent | ❌ |
| DKIM | absent | ❌ |
| DMARC | absent | ❌ |

## Red Flags Identifiés

| # | Red Flag | Explication |
|---|----------|-------------|
| 1 | **Domaine non officiel** | `gitlab-secure.net` ≠ `gitlab.com` |
| 2 | **Pop-up de login dans la page** | GitLab n'intègre jamais de popup SSO dans une page web |
| 3 | **URL de barre d'adresse falsifiée en CSS** | Le rendu visuel imite le chrome du navigateur mais n'est pas réel |
| 4 | **Formulaire externe** | POST vers `gitlab-secure.net/steal.php` |
| 5 | **"Repository partagé"** | Leurre classique pour les développeurs — curiosité professionnelle |
| 6 | **Absence de notification GitLab** | Pas de vrai email de GitLab, pas de notification dans l'interface |

## Déclencheurs Cognitifs

- **Curiosité** : "projet-strategique-2026", "partagé par un collègue"
- **Confiance** : Apparence d'une popup SSO légitime
- **Peur de manquer** : Projet stratégique — sentiment d'exclusion

## Analyse Technique — BitB

Le BitB est une attaque avancée :
1. L'email contient un lien vers une page HTML qui imite GitLab
2. Sur cette page, une popup est rendue en HTML/CSS/JS dans le DOM
3. La popup imite parfaitement la fenêtre SSO Google/GitLab
4. La barre d'adresse de la "popup" est du texte CSS — pas une vraie barre de navigateur
5. La popup ne peut pas être déplacée hors de la fenêtre parente

**Test simple** : Essayer de déplacer la popup — si elle reste dans les limites de la page, c'est du BitB.

## Classification
- **Verdict** : 🔴 **Malicious**
- **Justification** : BitB — hameçonnage SSO avancé avec popup falsifiée

## Décision de Triage
- **Action** : 🚫 **Block & Escalate**
- **Recommandation** : Vérifier l'URL dans la barre d'adresse réelle du navigateur (pas dans la popup), signaler au SOC

## IOCs Extracted

| Type | Valeur |
|------|--------|
| Domaine | gitlab-secure.net |
| Email | security@gitlab-secure.net |
| URL POST | https://gitlab-secure.net/steal.php |
| Leurre | projet-strategique-2026 |
