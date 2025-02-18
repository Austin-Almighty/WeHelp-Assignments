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

connection = mysql.connector.connect(**config)
cursor = connection.cursor()

@app.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request})

@app.get('/member')
def success(request: Request):
    if request.session.get("SIGNED-IN"):
        return templates.TemplateResponse('base.html',
            context={
                'request': request, 
                'page_title': '歡迎光臨，這是會員頁', 
                'message': '，歡迎登入系統',
                'signout': '登出系統',
                'member': request.session.get("name")
                 })
    else:
        return RedirectResponse('/')

@app.get('/error')
def error(request: Request, message: str = Query(default="登入失敗")):
    return templates.TemplateResponse("base.html",
        context={
            "request": request,
            "page_title": "失敗頁面",
            "message": message,
            "return": "返回首頁"
        }
    )

@app.post('/signup')
def signup(request: Request, name:Annotated[str, Form()], username:Annotated[str, Form()], password:Annotated[str, Form()]):
    cursor.execute("select username from member where username = %s", (username,))
    search = cursor.fetchone()

    if search:
         return RedirectResponse('/error?message=Repeated+username')
    else:
         cursor.execute("insert into member(name, username, password) values (%s, %s, %s);", (name, username, password))
         connection.commit()
         return RedirectResponse('/')
         

@app.post('/signin')
def signin(request: Request, username:Annotated[str, Form()], password:Annotated[str, Form()]):
    cursor.execute("select username, password from member where username = %s and password = %s", (username, password))
    result = cursor.fetchone()

    if result:
        cursor.execute("select name, username from member where username = %s", (username,))
        result = cursor.fetchone()
        request.session["SIGNED-IN"] = True
        request.session["name"] = result[0]
        request.session["username"] = result[1]
        return RedirectResponse('/member', status_code=303)
    else:
        return RedirectResponse('/error?message=Username+or+password+is+not+correct', status_code=303)


@app.get('/signout')
def signout(request: Request):
    request.session["SIGNED-IN"] = False
    request.session["name"] = None
    request.session["username"] = None
    request.session["password"] = None
    request.session.clear()
    return RedirectResponse('/')
