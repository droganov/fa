from app.app import v1, client

from pydantic import BaseModel


class Hello(BaseModel):
    hello: str


@v1.get("/")
def e1() -> Hello:
    return Hello(hello="World!")


def test_e1():
    response = client.get("/v1/")
    assert response.status_code == 200
    assert response.json() == {"hello": "World!"}
