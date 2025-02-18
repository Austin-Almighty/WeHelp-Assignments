from fastapi import FastAPI, Request, Path, Query, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated
from starlette.middleware.sessions import SessionMiddleware
from config import config
import mysql.connector

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key='WeHelp')

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# connection = mysql.connector.connect(**config)
# cursor = connection.cursor()
# cursor.execute
# connection.commit()

# connection.close()

@app.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request})

@app.get('/member')
def success(request: Request):
    return templates.TemplateResponse('base.html', context={'request': request, 'page_title': '歡迎光臨，這是會員頁', 'message': 'Austin，歡迎登入系統'})

@app.get('/error')
def error(request: Request, message: str = Query(default="登入失敗")):
    return templates.TemplateResponse("base.html",
        context={
            "request": request,
            "page_title": "失敗頁面",
            "message": message
        }
    )

@app.post('/signup')
def signup(request: Request):
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute("")

@app.post('signin')
def signin():

@app.get('/signout')
def signout(request: Request):
    request.session["SIGNED-IN"] = False
    return RedirectResponse(url="/")
