# PUT/put_with_path.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# two categories, each with their own items
fake_db = {
    "electronics": {
        1: {"name": "Laptop", "price": 999.99, "in_stock": True},
        2: {"name": "Mouse", "price": 29.99, "in_stock": True},
    },
    "furniture": {
        1: {"name": "Chair", "price": 199.99, "in_stock": False},
    }
}

# all fields required since this is a full update
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool


# two path params here, category and item_id both come from the URL
@app.put("/categories/{category}/items/{item_id}")
def update_item_in_category(category: str, item_id: int, item: Item):
    if category not in fake_db:
        return {"error": "category not found"}
    if item_id not in fake_db[category]:
        return {"error": "item not found in this category"}

    # fully replace the item with whatever the client sent
    fake_db[category][item_id] = item.model_dump()

    return {
        "message": f"item {item_id} in '{category}' updated successfully",
        "item": fake_db[category][item_id]
    }