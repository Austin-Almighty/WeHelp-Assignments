from fastapi import FastAPI, Request, Path, Query
from typing import Annotated
app = FastAPI()

@app.get("/")
def index():
    return "This is the index"



