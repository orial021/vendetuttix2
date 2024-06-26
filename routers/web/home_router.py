from fastapi import APIRouter, Request
from fastapi.responses import FileResponse, RedirectResponse, PlainTextResponse
from templates import templates


home_router = APIRouter()


@home_router.get('/', tags=['Home'])
def go_home():
    return RedirectResponse('/home')

@home_router.get('/home', tags=['Home'], response_class=FileResponse)
def home():
    return "<p>Hello Jairo</p>"

@home_router.get('/page')
def index(request: Request):
    return templates.TemplateResponse('home/index.html', {'request': request})