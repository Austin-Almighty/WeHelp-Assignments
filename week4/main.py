from fastapi import FastAPI, Request, Path, Query, Form
from fastapi.responses import RedirectResponse, HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    # return templates.TemplateResponse("index.html", context={"request": request})
    return FileResponse("index.html")


VALID_USERNAME = 'test'
VALID_PASSWORD = 'test'

@app.post('/signin')
async def signin(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username, "password": password}
    # if username == VALID_USERNAME and password == VALID_PASSWORD:
    #     return RedirectResponse("/member")
    # else:
    #     return RedirectResponse("/error")

@app.get('/member', response_class=HTMLResponse)
async def success(request: Request):
    return templates.TemplateResponse("base.html", context={"request": request, "page_title": "歡迎光臨，這是會員頁 ", "message": "恭喜您，成功登入系統"})

@app.get('/error', response_class=HTMLResponse)
async def error(request: Request):
    return templates.TemplateResponse("base.html", context={"request": request, "page_title": "失敗頁面", "message": "Invalid username or password. Please try again."})





