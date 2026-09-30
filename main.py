from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel


app = FastAPI(title="Name API")
HTML_FILE = Path(__file__).with_name("index.html")


class Name(BaseModel):
    firstName: str
    surName: str


stored_names: list[Name] = []


@app.get("/", include_in_schema=False)
async def index() -> FileResponse:
    return FileResponse(HTML_FILE)


@app.put("/putName", response_model=Name)
async def put_name(name: Name) -> Name:
    stored_names.append(name)
    return name


@app.get("/getNames", response_model=list[Name])
async def get_names() -> list[Name]:
    return stored_names
