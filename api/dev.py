from fastapi.staticfiles import StaticFiles
from starlette.types import Receive, Scope, Send

app_static = StaticFiles(directory="public", html=True)


class RedirectStaticFiles(StaticFiles):
    async def __call__(
        self, scope: Scope, receive: Receive, send: Send
    ) -> None:
        origin_response = await super().__call__(scope, receive, send)
        # origin_response

        return origin_response
