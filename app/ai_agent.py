import os
from typing import Optional

try:
    from transformers import pipeline
except Exception:
    pipeline = None

class AIAgent:
    def __init__(self, model_name: str = "local-small"):
        self.model_name = model_name
        self._init_model()

    def _init_model(self):
        self.openai_key = os.getenv("OPENAI_API_KEY")
        if pipeline and self.model_name.startswith("local") :
            try:
                self.generator = pipeline("text-generation", model="gpt2")
            except Exception:
                self.generator = None
        else:
            self.generator = None

    def generate(self, prompt: str, max_tokens: int = 256) -> str:
        if self.generator:
            out = self.generator(prompt, max_length=len(prompt.split()) + max_tokens, do_sample=True)
            return out[0]["generated_text"]

        if self.openai_key:
            import requests
            headers = {"Authorization": f"Bearer {self.openai_key}", "Content-Type": "application/json"}
            data = {"model": "gpt-4o-mini", "prompt": prompt, "max_tokens": max_tokens}
            resp = requests.post("https://api.openai.com/v1/completions", json=data, headers=headers, timeout=15)
            if resp.ok:
                j = resp.json()
                return j.get("choices", [{}])[0].get("text", "")
            return "(openai error)"

        return "(no model available — set OPENAI_API_KEY or enable local transformers)"
