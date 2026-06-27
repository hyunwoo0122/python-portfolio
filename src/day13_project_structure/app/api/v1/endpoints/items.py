from fastapi import APIRouter
from app.schemas.item import Item

router = APIRouter()

items = {}

# Path Parameter
@router.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}


# Query Parameter
@router.get("/items")
def get_items(
    skip: int = 0,
    limit: int = 10,
):
    return {
        "skip": skip,
        "limit": limit,
    }


# POST
@router.post("/items")
def create_item(item: Item):
    items[item.id] = item.name

    return {
        "message": "Item created"
    }