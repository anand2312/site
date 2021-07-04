import random

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request


app = FastAPI(docs_url=None, redoc_url=None)

app.mount("/static", StaticFiles(directory="./src/static"), name="static")

templates = Jinja2Templates(directory="./src/templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    favicon = f"/static/images/favicon-{random.randint(1, 3)}.webp"
    return templates.TemplateResponse(
        "index.html", {"request": request, "favicon": favicon}
    )
