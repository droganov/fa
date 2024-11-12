from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.providers.bugsnag import bugsnag_notify

app = FastAPI()


@app.exception_handler(Exception)
async def unicorn_exception_handler(request: Request, exc: Exception):
    bugsnag_notify(exc)
    return JSONResponse(
        status_code=500,
        content={"error": str(exc)},
    )


@app.get("/")
def read_root():
    return {"Hello": "World"}
