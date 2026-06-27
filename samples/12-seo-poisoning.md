# Sample 12 — SEO Poisoning : Faux site de login

## Raw Message

```
La cible n'a pas reçu d'email. Elle a cherché sur Google :

🔎 "Canva login" ou "Canva connexion"

--- Résultat Google (position sponsorisée) ---

[ ANNONCE ]
🏆 Canva — Connexion sécurisée
https://www.canva-login.top/
"Accédez à votre espace de travail Canva.
Éditeur graphique en ligne — gratuit et facile.
Plus de 100 millions d'utilisateurs."

--- Page de destination ---

URL : https://www.canva-login.top/
Certificat : Let's Encrypt (valide)
Design : Copie conforme de la page de connexion Canva
Code : HTML/CSS/JS identique, formulaire POST vers :

    https://www.canva-login.top/steal-credentials.php

Le domaine a été enregistré il y a 4 jours.
10 pages de contenu SEO bidon pour remonter dans les résultats.
Aucune balise meta noindex — le site est indexé par Google.

--- Technique ---
L'assaillant achète des publicités Google Ads pointant vers
son site, ou utilise du black hat SEO (PBN, cloaking) pour
se positionner en haut des résultats organiques.
```
