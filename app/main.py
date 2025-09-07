from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
from app.ai_agent import AIAgent
from app.webhooks import handle_x_webhook

app = FastAPI(title="NeuraLabzAI Utility")
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Initialize agent once
AI_MODEL = os.getenv("NLZAI_MODEL", "openai-gpt")
agent = AIAgent(model_name=AI_MODEL)

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/generate")
async def generate(request: Request, background_tasks: BackgroundTasks):
    payload = await request.json()
    prompt = payload.get("prompt", "")
    if not prompt:
        return JSONResponse({"error": "prompt required"}, status_code=400)

    # run generate (sync wrapper)
    result = agent.generate(prompt)

    # optionally enqueue posting to social channels
    if payload.get("post_to_social"):
        background_tasks.add_task(handle_x_webhook, result)

    return {"result": result}

@app.post("/webhook/x")
async def x_webhook(request: Request):
    payload = await request.json()
    # Very small validator; production should validate signatures
    background_tasks = BackgroundTasks()
    background_tasks.add_task(handle_x_webhook, payload)
    return {"status": "accepted"}
