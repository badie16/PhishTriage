# Sample 01 — Fausse alerte de sécurité bancaire

## Raw Message

```
From:     "Sécurité Banque Nationale" <no-reply@securite-banque-nationale.xyz>
Reply-To: fraud@phisher.io
Return-Path: bounce@phisher.io
To:       client@gmail.com
Subject:  ⚠️ Activité suspecte détectée sur votre compte

--- Message Body ---

Cher client,

Nous avons détecté une connexion suspecte depuis un appareil non reconnu
(IP: 185.220.101.23, localisation: Russie).

Pour sécuriser votre compte, veuillez confirmer votre identité dans les
plus brefs délais via le lien sécurisé ci-dessous :

👉 https://securite-banque-nationale.xyz/verify/identite

Si vous ne confirmez pas sous 24 heures, votre compte sera temporairement
suspendu.

Merci de votre compréhension.

L'équipe Sécurité Banque Nationale

--- Headers bruts ---
Received: from mail.phisher.io (mail.phisher.io [192.168.1.100])
 by mx.google.com with ESMTP id abc123
DKIM-Signature: v=1; a=rsa-sha256; d=phisher.io; s=default;
 c=relaxed/relaxed; bh=abc123def456=
SPF: fail (phisher.io not authorized for banque-nationale.com)
DMARC: fail (quarantine)
```
