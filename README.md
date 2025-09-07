# NeuraLabzAI Utility

Starter repo for NeuraLabzAI — FastAPI service + AI agent + crypto hooks + social posting skeleton.

## Quick start
1. Copy `.env.example` to `.env` and add keys.
2. Build & run with Docker Compose: `docker compose up --build` or run directly: `uvicorn app.main:app --reload --port 8080`
3. POST to `/api/generate` with JSON: `{ "prompt": "Write a short DeSci announcement for NeuraLabzAI", "post_to_social": true }`

## Notes
- Replace placeholders (crypto adapters, OAuth, OpenAI usage) before production.
- Secure keys with GitHub Secrets / Vault for deployments.
