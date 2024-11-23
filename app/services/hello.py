from pydantic import BaseModel


class Hello(BaseModel):
    hello: str


def say_hello():
    return Hello(hello="World!")
