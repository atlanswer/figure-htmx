from fastapi.exceptions import StarletteHTTPException
from typing import Awaitable, Callable
import typing

from fastapi import Request, Response
from fastapi.staticfiles import StaticFiles
from starlette.types import Message
from main import app

app_static = StaticFiles(directory="public", html=True)


@app.middleware("http")
async def redirect_static_file(
    req: Request, call_next: Callable[[Request], Awaitable[Response]]
):
    res = Response()

    async def send(msg: Message) -> typing.NoReturn:
        if "status" in msg:
            res.status_code = msg["status"]
        if "headers" in msg:
            res.raw_headers = msg["headers"]
        res.body += msg.get("body", b"")

    try:
        await app_static(req.scope, req.receive, send)
    except StarletteHTTPException as e:
        if e.status_code != 404:
            raise e
        res = await call_next(req)

    return res
