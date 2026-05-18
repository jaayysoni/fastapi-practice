# POST/body_with_path.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool

@app.post("/users/{user_id}/items/")
def create_item_for_user(user_id: int, item: Item):
    return {
        "Messaeg": "Item created successfully",
        "user_id": user_id,
        "item": item
    }




