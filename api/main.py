from typing import Union

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/items/{item_id}")
async def get_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
