# Sample 11 — TOAD : Callback Phishing

## Raw Message

```
From:     "Service Abonnement" <info@facturation-paypal-safe.com>
Reply-To: support@facturation-paypal-safe.com
To:       client@email.com
Subject:  🧾 Facture PayPal #INV-2026-7843 — 549,99€

--- Message Body ---

Bonjour,

Nous vous confirmons l'achat suivant sur votre compte PayPal :

📦 Abonnement Premium Sécurité — 549,99€
📅 Date : 27/06/2026
🆔 Réf : INV-2026-7843

SI VOUS N'AVEZ PAS EFFECTUÉ CET ACHAT, APPELEZ LE :
📞 0 891 45 67 89 (Service Litiges — ouvert 7j/7)

Nos conseillers sont à votre disposition pour vous accompagner
dans la procédure d'annulation et de remboursement.

Ne répondez pas à cet email. Contactez-nous par téléphone.

Merci de votre confiance,
L'équipe PayPal Sécurité

--- Mécanisme TOAD ---
1. La cible reçoit une fausse facture
2. Paniquée, elle appelle le numéro surtaxé
3. L'assaillant lui demande :
   - ses identifiants bancaires "pour le remboursement"
   - ou d'installer un logiciel de prise en main à distance
4. Vol de compte / ransomware
```
