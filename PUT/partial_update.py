#PUT/partial_update.py

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

fake_db = {
    1: {"name": "Laptop", "price": 999.99, "in_stock": True },
    2: {"name": "Mouse", "price": 29.99, "in_stock": True},
}

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    in_stock: Optional[bool] = None

@app.put("/items/{item_id}")
def partial_update(item_id: int,item: ItemUpdate ):
    if item_id not in fake_db:
        return{"error": "item not found"}
    
    existing = fake_db[item_id]
    updated_fields = item.model_dump(exclude_unset = True)
    existing.update(updated_fields)

    return {"message": "item partially updated successfully"," item": fake_db[item_id] }

@app.patch("/items/{item_id}")
def partial_update(item_id: int,item: ItemUpdate):
    if item_id not in fake_db:
        return {"error": "item not found"}
    existing = fake_db[item_id]
    updated_fileds = item.model_dump(exclude_unset = True)
    existing.update(updated_fileds)

    return {"message": "item partially updated successfully", "item": fake_db[item_id]}











































