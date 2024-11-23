from app.framework.app import v1, client
from app.services.hello import say_hello


@v1.get("/", operation_id="hello", summary="V1 home")
def hello():
    """Hello World endpoint"""
    return say_hello()


def test_hello():
    response = client.get("/v1/")
    assert response.status_code == 200
    assert response.json() == {"hello": "World!"}
