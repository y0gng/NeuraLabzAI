# NeuraLabzAI Utility

NeuraLabzAI Utility is a full starter framework combining AI, decentralized science (DeSci), and crypto functionality. Includes:
- FastAPI web server for serving AI content
- AI agent (local or OpenAI) for generating text
- Crypto adapter for token and liquidity operations (placeholder for Solana/Raydium)
- Worker system for async tasks and social posting (X/Twitter, Telegram)
- Dockerized deployment and CI setup


## Quick start
1. Copy `.env.example` to `.env` and add keys.
2. Build & run with Docker Compose: `docker compose up --build` or run directly: `uvicorn app.main:app --reload --port 8080`
3. POST to `/api/generate` with JSON: `{ "prompt": "Write a short DeSci announcement for NeuraLabzAI", "post_to_social": true }`

## Notes
- Replace placeholders (crypto adapters, OAuth, OpenAI usage) before production.
- Secure keys with GitHub Secrets / Vault for deployments.

Follow us on X: https://x.com/NeuraLabz
