from fastapi import FastAPI, Request, Query, Form
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated
from starlette.middleware.sessions import SessionMiddleware
from config import config
import mysql.connector

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key='WOIJFOINOJNFOIJA')

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

connection = mysql.connector.connect(**config)


@app.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request})

@app.get('/member')
def success(request: Request):
    if request.session.get("SIGNED-IN"):
        cursor = connection.cursor()
        cursor.execute('select member.name, message.content, message.member_id, message.id from member INNER JOIN message ON member.id = message.member_id order by message.time;')
        messages = cursor.fetchall()
        return templates.TemplateResponse('member.html',
            context={
                'request': request, 
                'page_title': '歡迎光臨，這是會員頁', 
                'message': '，歡迎登入系統',
                'signout': '登出系統',
                'member': request.session.get("name"),
                'messages': messages
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
    cursor = connection.cursor()
    cursor.execute("select username from member where username = %s", (username,))
    search = cursor.fetchone()

    if search:
         return RedirectResponse('/error?message=Repeated+username', status_code=303)
    else:
         cursor.execute("insert into member(name, username, password) values (%s, %s, %s);", (name, username, password))
         connection.commit()
         return RedirectResponse('/', status_code=303)
         

@app.post('/signin')
def signin(request: Request, username:Annotated[str, Form()], password:Annotated[str, Form()]):
    cursor = connection.cursor()
    cursor.execute("select name, username, id from member where username = %s and password = %s", (username, password))
    result = cursor.fetchone()

    if result:
        request.session["SIGNED-IN"] = True
        request.session["name"] = result[0]
        request.session["username"] = result[1]
        request.session["member_id"] = result[2]
        return RedirectResponse('/member', status_code=303)
    else:
        return RedirectResponse('/error?message=Username+or+password+is+not+correct', status_code=303)


@app.get('/signout')
def signout(request: Request):
    request.session["SIGNED-IN"] = False
    request.session["name"] = None
    request.session["username"] = None
    request.session["member_id"] = None
    request.session.clear()
    return RedirectResponse('/')

@app.post('/createMessage')
def create(request: Request, comment_box:Annotated[str, Form()]):
    member_id = request.session.get("member_id")
    comment = comment_box.strip()
    cursor = connection.cursor()
    cursor.execute("insert into message(member_id, content) values(%s, %s);", (member_id, comment))
    connection.commit()
    return RedirectResponse('/member', status_code=303)

@app.post('/deleteMessage')
def delete(request: Request, message_id:Annotated[int, Form()]):
    if not request.session.get("SIGNED-IN"):
        return RedirectResponse('/', status_code=303)
    
    member_id = request.session.get('member_id')
    cursor = connection.cursor()
    cursor.execute("select id from message where id = %s and member_id = %s;", (message_id, member_id))
    message = cursor.fetchone()

    if message:
        cursor.execute("delete from message where id = %s;", (message_id,))
        connection.commit()
    return RedirectResponse("/member", status_code=303)

@app.get('/api/member')
def api(request: Request, username:Annotated[str, Query()]):
    if not request.session.get("SIGNED-IN", False):
        return JSONResponse({'data':None})
    cursor = connection.cursor()
    cursor.execute('select id, name, username from member where username = %s;', (username,))
    member = cursor.fetchone()
    if not member:
        return JSONResponse({'data':None})
    else:
        return JSONResponse({'data':{"id":member[0], "name":member[1], "username":member[2]}})