from app.routers import v1

from pydantic import BaseModel


class Hello(BaseModel):
    hello: str


@v1.get("/")
def ep1() -> Hello:
    return Hello(hello="World!")
