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
    return templates.TemplateResponse("index.html", context={"request": request})

@app.get("/square/{positive}")
def sqaure(positive:Annotated[int, None], request: Request):
    result = int(positive) * int(positive)
    return templates.TemplateResponse('base.html', context={"request": request, "page_title": "正整數平方計算結果", "message": result})


VALID_USERNAME = 'test'
VALID_PASSWORD = 'test'

@app.post('/signin')
async def signin(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    if len(username.strip()) == 0 or len(password.strip()) == 0:
        return RedirectResponse(url="/error?message=Please+enter+username+and+password", status_code=303)
    elif username == VALID_USERNAME and password == VALID_PASSWORD:
        return RedirectResponse(url="/member", status_code=303)
    else:
        return RedirectResponse(url="/error?message=Username+or+password+is+not+correct", status_code=303)


@app.get('/member', response_class=HTMLResponse)
async def success(request: Request):
    return templates.TemplateResponse("base.html", context={"request": request, "page_title": "歡迎光臨，這是會員頁 ", "message": "恭喜您，成功登入系統"})


@app.get('/error', response_class=HTMLResponse)
async def error(request: Request, message: str = Query(default="登入失敗")):
    return templates.TemplateResponse("base.html",
        context={
            "request": request,
            "page_title": "失敗頁面",
            "message": message
        }
    )





