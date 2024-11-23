from app.framework.app import v1, client
from app.services.hello import hello


@v1.get("/")
def e1():
    return hello()


def test_e1():
    response = client.get("/v1/")
    assert response.status_code == 200
    assert response.json() == {"hello": "World!"}
