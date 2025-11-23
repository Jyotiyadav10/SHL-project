from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from recommend import recommend_assessments

app = FastAPI()

# Serve /statics folder
app.mount("/statics", StaticFiles(directory="../frontend/statics"), name="statics")

# Serve templates
templates = Jinja2Templates(directory="../frontend/templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/health")
def health():
    return {"status": "API is running"}

@app.post("/recommend")
def recommend_api(data: dict):
    text = data.get("text", "")
    top_k = data.get("top_k", 5)
    recs = recommend_assessments(text, top_k)
    return {"query": text, "recommendations": recs}
