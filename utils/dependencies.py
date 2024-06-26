'''import os
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates



def init_app(app):
    static_path = os.path.join(os.path.dirname(__file__), '/src/static/css')
    templates_path = os.path.join(os.path.dirname(__file__), '/src/templates')

    app.mount('/static', StaticFiles(directory=static_path), 'static')
    templates = Jinja2Templates(directory=templates_path)
    return templates'''
