from fastapi import FastAPI, Request, Path, Query, Form
from fastapi.responses import FileResponse, RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated, Optional

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})

@app.get('/error', response_class=HTMLResponse)
async def error(
    request: Request,
):
    context = {
        "request": request,
        "page_title": "失敗頁面",
        "message": "missing info"
    }
    return templates.TemplateResponse('base.html', context=context)


@app.post('/signin', response_class=HTMLResponse)
def signin(username:Annotated[str, Form()], password:Annotated[str, Form()], request: Request):
    if len(username) == 0 or len(password) == 0:
        # context = {'request': request,
        #            "page_title": "失敗頁面",
        #            "message": "Please enter your username and password"
        # }
        return RedirectResponse(url="/error?message=Please+enter+your+username+and+password", status_code=302)
    # elif username == "test" and password == "test":
    #     return RedirectResponse('/member')
    # else:
    #     return RedirectResponse('/error')


# @app.get('/error')
# def error(message):
#     if 

# @app.get('/member')
# def 




