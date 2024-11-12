from fastapi import APIRouter, FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

v1 = APIRouter()

client = TestClient(app)
