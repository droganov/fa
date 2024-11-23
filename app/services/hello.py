from pydantic import BaseModel


class Hello(BaseModel):
    hello: str


def hello():
    return Hello(hello="World!")
