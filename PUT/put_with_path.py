# PUT/put_with_path.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# nested db, category is the outer key, item_id is the inner key
fake_db = {
    "electronics": {
        1: {"name": "Laptop", "price": 999.99, "in_stock": True},
        2: {"name": "Mouse", "price": 29.99, "in_stock": True},
    },
    "furniture": {
        1: {"name": "Chair", "price": 199.99, "in_stock": False},
    }
}

# full update model, all fields required, client must send everything
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool


# both category and item_id come from the URL, not the body
# URL pattern: /categories/electronics/items/1
@app.put("/categories/{category}/items/{item_id}")
def update_item_in_category(category: str, item_id: int, item: Item):

    # check outer level first, does the category exist
    if category not in fake_db:
        return {"error": "category not found"}

    # then check inner level, does the item exist inside that category
    if item_id not in fake_db[category]:
        return {"error": "item not found in this category"}

    # fully replace the item, old data is gone, new data takes its place
    fake_db[category][item_id] = item.model_dump()

    return {
        "message": f"item {item_id} in '{category}' updated successfully",
        "item": fake_db[category][item_id]
    }






