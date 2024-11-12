from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from os import path
import glob
import importlib

from app.providers.bugsnag import bugsnag_notify
from app.routers import v1

app = FastAPI()


@app.exception_handler(Exception)
async def unicorn_exception_handler(request: Request, exc: Exception):
    bugsnag_notify(exc)
    return JSONResponse(
        status_code=500,
        content={"error": str(exc)},
    )


current_dir = path.dirname(__file__)
endpoint_files = glob.glob(path.join(current_dir, "**", "*_route.py"), recursive=True)


for file_path in endpoint_files:
    if "__init__" in file_path:
        continue

    relative_path = path.relpath(file_path, current_dir)
    module_path = "app." + ".".join(path.splitext(relative_path)[0].split(path.sep))
    importlib.import_module(module_path)

app.include_router(v1, prefix="/v1", tags=["v1"])
