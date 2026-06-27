# Analyse 10 — MFA Fatigue : Saturation push

## Référence
- **Échantillon** : `samples/10-mfa-fatigue.md`
- **Vecteur** : Email (préparation) + Push notifications MFA (attaque)
- **Source** : alert@security-notifications.tk

## Analyse des en-têtes

| Champ | Valeur | Verdict |
|-------|--------|---------|
| From | "IT Security Alert" <alert@security-notifications.tk> | ❌ Domaine .tk |
| Reply-To | alert@security-notifications.tk | ❌ Domaine frauduleux |
| SPF | absent | ❌ |
| DKIM | absent | ❌ |
| DMARC | absent | ❌ |

## Red Flags Identifiés

| # | Red Flag | Explication |
|---|----------|-------------|
| 1 | **Domaine .tk** | Domaine gratuit — aucune légitimité |
| 2 | **Email préparatoire** | L'email prévient la cible qu'elle va recevoir des notifications → réduit la méfiance |
| 3 | **23 tentatives en 5 minutes** | Chiffre cohérent avec une attaque par saturation |
| 4 | **IPs multiples / pays variés** | Indique une attaque distribuée (proxy/VPN) |
| 5 | **"Approuvez uniquement si..."** | Instruction contradictoire qui noie la cible |
| 6 | **Numéro SOC suspect** | +33 1 55 66 77 88 — à vérifier hors bande |

## Déclencheurs Cognitifs

- **Peur** : "23 tentatives de connexion échouées"
- **Confusion** : Notifications push répétées → fatigue décisionnelle
- **Autorité** : "IT Security Alert", "SOC"

## Analyse Technique — MFA Fatigue

1. L'attaquant a déjà le mot de passe de la cible (fuite / credential stuffing)
2. Le MFA est activé — il ne peut pas se connecter sans validation
3. Il envoie des centaines de requêtes MFA en rafale
4. La cible reçoit des notifications push continues
5. Par lassitude ou distraction, la cible finit par approuver
6. L'attaquant valide immédiatement sa session

**Cas réel** : Uber (2022), Microsoft (2023), MGM/Cesars (2023)

## Classification
- **Verdict** : 🔴 **Malicious**
- **Justification** : Attaque MFA Fatigue — saturation de notifications push

## Décision de Triage
- **Action** : 🚫 **Block & Escalate**
- **Procédure** : 
  1. NE PAS approuver les notifications
  2. Contacter le SOC par un canal différent
  3. Révoquer les sessions actives
  4. Réinitialiser le mot de passe immédiatement

## IOCs Extracted

| Type | Valeur |
|------|--------|
| Domaine | security-notifications.tk |
| Email | alert@security-notifications.tk |
| IP Range | 185.220.101.0/24 |
| IP Range | 91.121.87.0/24 |
| IP Range | 45.33.32.0/24 |
| Numéro (à vérifier) | +33 1 55 66 77 88 |
