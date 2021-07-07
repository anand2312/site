import itertools
from typing import Any

from decouple import config
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from loguru import logger
from starlette.requests import Request
from starlette.responses import Response

from src.gh_api import GHApiClient


async def handle_404(
    request: Request, exc: Any
) -> Response:  # i don't wanna annotate this :(
    logger.warning(f"404 reached on {request.url}, showed error page")
    return templates.TemplateResponse(
        "404.html",
        {"request": request, "favicon": get_favicon(), "title": "404"},
        status_code=404,
    )


def get_favicon() -> str:
    """Function to get the favicon by cycling through the cat chan images."""
    return f"/static/images/favicon-{next(favicon_number)}.webp"


app = FastAPI(docs_url=None, redoc_url=None, exception_handlers={404: handle_404})
app.mount("/static", StaticFiles(directory="./src/static"), name="static")
templates = Jinja2Templates(directory="./src/templates")

favicon_number = itertools.cycle(range(1, 3))

api_client = GHApiClient(token=config("API_TOKEN"))

basic_template_ctx = {"favicon": get_favicon()}  # extend this ctx in the views


@app.on_event("startup")
async def startup() -> None:
    """Start the GH API data collection."""
    api_client.start()


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "title": "Index", **basic_template_ctx}
    )


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse(
        "about.html",
        {"request": request, "title": "About Me", **basic_template_ctx},
    )


@app.get("/projects", response_class=HTMLResponse)
async def projects(request: Request):
    projects = api_client.get_projects()
    return templates.TemplateResponse(
        "projects.html",
        {
            "request": request,
            "projects": projects,
            "title": "Projects",
            **basic_template_ctx,
        },
    )
