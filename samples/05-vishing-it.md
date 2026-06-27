# Sample 05 — Vishing : Appel support IT

## Raw Message (Transcript)

```
Date de l'appel : 2026-06-27 10:15
Numéro entrant : 01 88 45 23 01 (affiche "Support Microsoft")
Durée : 3 min 42 sec

--- Script ---

Appelant : Bonjour, ici Thomas du support technique Microsoft.
           Nous avons détecté une intrusion sur votre poste de travail.
           Votre adresse IP 86.xx.xx.xx est compromise.

Cible :   ... hein ? Quoi comme intrusion ?

Appelant : Un ransomware a été détecté. On voit des connexions sortantes
           vers un serveur en Biélorussie. Il faut agir tout de suite.
           Je vais vous guider pour installer un outil de sécurisation
           à distance. Vous êtes devant votre ordinateur ?

Cible :   Euh oui mais...

Appelant : Parfait. Ouvrez Chrome et tapez : bit.ly/ms-secure-remote
           Ne vous inquiétez pas, c'est la procédure standard.

Cible :   Je sais pas, je préfère appeler mon service IT.

Appelant : Vous n'avez pas le temps. Dans 7 minutes votre disque dur
           sera chiffré. Vous voulez perdre toutes vos données ?

--- Analyse ---
Caller ID affiché : Microsoft Support (spoofé)
Numéro réel : +33 1 88 45 23 01 (VoIP jetable)
```
