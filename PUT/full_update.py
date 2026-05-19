#PUT/full_update.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


fake_db = {
    1: {"name": "Laptop", "price": 999.99, "in_stock": True },
    2: {"name": "Mouse", "price": 29.99, "in_stock": True},
}

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool

@app.put("/items/{item_id}")
def full_update(item_id: int,item:Item ):
    if item_id not in fake_db:
        return {"error": "Item not found"}
    fake_db[item_id] = item.model_dump()
    return {"message": "Item, fully updated successfully","item": fake_db[item_id] }





























