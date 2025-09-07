# Basic idea: use Celery or RQ. This file demonstrates tasks interfaces.

def generate_and_post(prompt: str, agent, poster):
    out = agent.generate(prompt)
    if "signal" in out.lower():
        poster.post_to_x(out)
    return out
