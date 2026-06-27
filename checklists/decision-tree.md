# 🌳 Arbre de Décision — PhishTriage

## Diagramme

```mermaid
graph TD
    START([📩 Message Suspect]) --> H1{Expéditeur connu<br>et attendu ?}
    
    H1 -->|Non| MAL[🔴 MALICIOUS]
    H1 -->|Oui| H2{Domaine = <br>site officiel ?}
    
    H2 -->|Non| H21{Typosquatting /<br>Homoglyph ?}
    H21 -->|Oui| MAL
    H21 -->|Non| H22{Âge domaine<br>> 6 mois ?}
    H22 -->|Non| MAL
    H22 -->|Oui| SUSP
    
    H2 -->|Oui| H3{SPF / DKIM / DMARC<br>valides ?}
    H3 -->|Non| MAL
    H3 -->|Oui| H4{Message demande<br>action sensible ?}
    
    H4 -->|Non| H41{Pièce jointe<br>inattendue ?}
    H41 -->|Oui| H42{Extension<br>dangereuse ?}
    H42 -->|Oui (.docm/.exe/...) | MAL
    H42 -->|Non (.pdf/.txt) | SUSP
    H41 -->|Non| SAFE([🟢 SAFE → Close])
    
    H4 -->|Oui| H5{Urgence artificielle<br>présente ?}
    H5 -->|Oui| MAL
    H5 -->|Non| H6{Nombre de<br>déclencheurs > 2 ?}
    H6 -->|Oui| SUSP([🟡 SUSPICIOUS → Warn User])
    H6 -->|Non| H7{Demande via<br>canal habituel ?}
    H7 -->|Oui| SAFE
    H7 -->|Non| SUSP

    MAL --> MAL_ACT[🚫 Block & Escalate]
    SUSP --> SUSP_ACT[⚠️ Warn User + Vérification hors bande]
    SAFE --> SAFE_ACT[✅ Fermer / Close]
```

## Table de décision rapide

| Scénario | Domaine | SPF/DKIM/DMARC | Demande sensible | Urgence | Verdict |
|----------|---------|---------------|-----------------|---------|---------|
| Email banque légitime | ✅ OK | ✅ Pass | ❌ Non | ❌ Non | 🟢 Safe |
| Alerte sécurité banque | ❌ .xyz | ❌ Fail | ✅ Oui | ✅ Oui | 🔴 Malicious |
| Virement PDG urgent | ❌ billing.com | ❌ Absent | ✅ Virement | ✅ Oui | 🔴 Malicious |
| Doc RH confidentiel | ❌ .net | ❌ Absent | ✅ PJ .docm | ❌ Non | 🔴 Malicious |
| Colis DHL en attente | ❌ .top | N/A (SMS) | ✅ Paiement | ✅ Oui | 🔴 Malicious |
| Support Microsoft appel | ❌ Spoofé | N/A (Voice) | ✅ Accès distant | ✅ Oui | 🔴 Malicious |
| QR code sécurité M365 | ❌ .tk | ❌ Absent | ✅ Login | ✅ Oui | 🔴 Malicious |
| Suspension Google | ❌ g00gle | ❌ Absent | ✅ Login | ✅ Oui | 🔴 Malicious |
| Commande Amazon bloquée | ❌ Homoglyph | ❌ Absent | ✅ Annulation | ✅ Oui | 🔴 Malicious |
| Partage GitLab | ❌ .net | ❌ Absent | ✅ SSO Login | ❌ Non | 🔴 Malicious |
| MFA Fatigue | ❌ .tk | ❌ Absent | ✅ Approuver MFA | ✅ Oui | 🔴 Malicious |
| Facture PayPal TOAD | ❌ .com | ❌ Absent | ✅ Appel surtaxé | ✅ Oui | 🔴 Malicious |
| SEO Canva | ❌ .top | N/A (Search) | ✅ Login | ❌ Non | 🔴 Malicious |

## Logique de décision

```
SI Domaine ≠ site officiel → MALICIOUS
SINON SI SPF/DKIM/DMARC ≠ pass → MALICIOUS
SINON SI demande sensible + urgence → MALICIOUS
SINON SI demande sensible + >2 déclencheurs → SUSPICIOUS
SINON SI pièce jointe dangereuse → MALICIOUS
SINON SI pièce jointe non dangereuse mais inattendue → SUSPICIOUS
SINON → SAFE
```

## Instructions d'utilisation

1. Commencer par le **haut** du diagramme
2. Suivre les branches **Oui/Non**
3. Arriver à un **verdict** (🟢 / 🟡 / 🔴)
4. Appliquer l'**action** correspondante

### Règles d'or

- **En cas de doute → SUSPICIOUS** (ne jamais classer "safe" par défaut)
- **Vérification hors bande** obligatoire pour tout verdict suspicieux
- **Toute demande d'identifiants/mot de passe/virement = rouge immédiat**
- **Toute pièce jointe .docm/.exe/.vbs/.js = rouge immédiat**
