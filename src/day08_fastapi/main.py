from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

items = {}


class Item(BaseModel):
    id: int
    name: str


# Path Parameter
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}


# Query Parameter
@app.get("/items")
def get_items(
    skip: int = 0,
    limit: int = 10,
):
    return {
        "skip": skip,
        "limit": limit,
    }


# POST
@app.post("/items")
def create_item(item: Item):
    items[item.id] = item.name

    return {
        "message": "Item created"
    }