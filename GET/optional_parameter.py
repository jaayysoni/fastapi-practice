# GET/optional_parameter.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/by-name")
def get_items_by_name(name: str = None):
    if name:
        return {"message": f"Hello,{name}"}
    return {"message": "Hello,word"}

@app.get("/items/by-limit")
def get_items_by_limit(limit: int = 10):
    return {"message": f"Limit is {limit}"}


@app.get("/items/by-search")
def get_items_by_search(search: str | None = None):
    if search:
        return {"message": f"searching for {search}"}
    return {"message": "No Search Query Provided"}




