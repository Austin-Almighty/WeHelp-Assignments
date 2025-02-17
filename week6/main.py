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
cursor.execute
connection.commit()

connection.close()


@app.post()
def signin()