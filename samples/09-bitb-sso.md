# Sample 09 — BitB : Browser-in-the-Browser

## Raw Message

```
From:     "GitLab Security" <security@gitlab-secure.net>
Reply-To: security@gitlab-secure.net
To:       dev@entreprise.fr
Subject:  Accès à un repository partagé avec vous

--- Message Body ---

Bonjour,

Un repository privé a été partagé avec vous par un collègue :
"projet-strategique-2026" par Marc D.

Pour y accéder, connectez-vous via SSO :

[ FENÊTRE POPUP — FAUX SSO ]
┌──────────────────────────────────┐
│    Se connecter avec GitLab      │
│                                  │
│    ┌────────────────────────┐   │
│    │ user@entreprise.fr     │   │
│    └────────────────────────┘   │
│    ┌────────────────────────┐   │
│    │ *********************  │   │
│    └────────────────────────┘   │
│                                  │
│       [ Sign in ]               │
│                                  │
│    Authentification SSO Google  │
│    Powered by GitLab EE         │
└──────────────────────────────────┘

🔒 Connexion sécurisée via SSO Google.

--- Note technique ---
La popup est intégrée dans le DOM de la page (iframe / div overlay).
L'URL de la barre d'adresse est falsifiée en CSS.
Les credentials sont envoyés à : https://gitlab-secure.net/steal.php
```
