# Sample 10 — MFA Fatigue : Saturation push

## Raw Message

```
From:     "IT Security Alert" <alert@security-notifications.tk>
Reply-To: alert@security-notifications.tk
To:       admin@company.com
Subject:  [URGENT] Multiples tentatives de connexion échouées

--- Message Body ---

Bonjour,

Nous avons détecté 23 tentatives de connexion échouées sur votre
compte administrateur au cours des 5 dernières minutes.

Origine des tentatives :
- IP: 185.220.101.0/24 (Allemagne)
- IP: 91.121.87.0/24 (France)
- IP: 45.33.32.0/24 (États-Unis)

Pour sécuriser votre compte, vous allez recevoir des notifications
d'approbation MFA sur votre téléphone. Appuyez sur "Approuver"
uniquement si vous êtes à l'origine de la connexion.

⚠️ Si vous ne reconnaissez pas ces tentatives, contactez immédiatement
le SOC au +33 1 55 66 77 88.

--- Attaque en cours ---
L'attaquant envoie en parallèle des centaines de requêtes MFA
pour saturer l'utilisateur.
Objectif : l'utilisateur finit par approuver par fatigue.
```
