# Analyse 07 — Typosquatting : Google clone

## Référence
- **Échantillon** : `samples/07-typosquatting.md`
- **Vecteur** : Email (Typosquatting)
- **Source** : no-reply@g00gleworkspace.com

## Analyse des en-têtes

| Champ | Valeur | Verdict |
|-------|--------|---------|
| From | "Google Workspace" <no-reply@g00gleworkspace.com> | ❌ Domaine visuellement proche mais différent |
| Reply-To | admin@g00gleworkspace.com | ❌ Domaine frauduleux |
| SPF | probablement absent | ❌ |
| DKIM | absent | ❌ |
| DMARC | absent | ❌ |

## Red Flags Identifiés

| # | Red Flag | Explication |
|---|----------|-------------|
| 1 | **Typosquatting** | `g00gleworkspace.com` (zéro → lettre o) au lieu de `googleworkspace.com` |
| 2 | **Certificat SSL récent** | Let's Encrypt valide depuis 3 jours — rien ne garantit la légitimité |
| 3 | **Page de login clonée** | Copie conforme pour capturer les identifiants |
| 4 | **Menace de suspension** | "Suspendu dans 48 heures" — pression temporelle |
| 5 | **URL trompeuse** | `www.g00gleworkspace.com/verify` ressemble à la page officielle |
| 6 | **Aucun détail technique** | Pas de numéro de ticket, pas de référence administrateur |

## Déclencheurs Cognitifs

- **Peur** : "Suspension imminente", "perte définitive de l'accès"
- **Urgence** : "48 heures"
- **Confiance usurpée** : Logo et signature Google

## Analyse Technique

Le typosquatting exploite la similarité visuelle :
- `g00gle` remplace `google` (deux 'o' par des '0')
- Difficile à repérer dans un email ou une URL
- Certificat HTTPS valide → le cadenas vert rassure la cible
- Page HTML identique à la vraie page Google Workspace

## Classification
- **Verdict** : 🔴 **Malicious**
- **Justification** : Typosquatting — hameçonnage d'identifiants Google Workspace

## Décision de Triage
- **Action** : 🚫 **Block & Escalate**
- **Recommandation** : Signaler le domaine à Google Safe Browsing, bloquer au niveau DNS

## IOCs Extracted

| Type | Valeur |
|------|--------|
| Domaine | g00gleworkspace.com |
| Email | no-reply@g00gleworkspace.com |
| Email | admin@g00gleworkspace.com |
| URL | https://www.g00gleworkspace.com/verify |
| Certificat | Let's Encrypt (délivré 2026-06-24) |
