from typing import Awaitable, Callable
from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app_static = StaticFiles(directory="public", html=True)


@app.middleware("http")
async def redirect_static_file(
    req: Request, call_next: Callable[[Request], Awaitable[Response]]
):
    res = await call_next(req)
    return res
