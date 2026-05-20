# PUT/partial_update.py

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# fake database, resets every time you restart the server
fake_db = {
    1: {"name": "Laptop", "price": 999.99, "in_stock": True},
    2: {"name": "Mouse", "price": 29.99, "in_stock": True},
}

# all fields are Optional so client can send only what they want to change
class ItemUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    in_stock: Optional[bool] = None


# PUT version of partial update, not semantically pure but works for learning
@app.put("/items/{item_id}")
def put_partial_update(item_id: int, item: ItemUpdate):
    if item_id not in fake_db:
        return {"error": "item not found"}

    existing = fake_db[item_id]

    # only grab the fields the client actually sent, ignore the rest
    updated_fields = item.model_dump(exclude_unset=True)

    # merge into existing record, untouched fields stay as they are
    existing.update(updated_fields)

    return {"message": "item partially updated successfully", "item": fake_db[item_id]}


# PATCH is the correct HTTP method for partial updates
@app.patch("/items/{item_id}")
def patch_partial_update(item_id: int, item: ItemUpdate):
    if item_id not in fake_db:
        return {"error": "item not found"}

    existing = fake_db[item_id]

    # same logic, only sent fields get picked up
    updated_fields = item.model_dump(exclude_unset=True)

    # only those fields get updated, everything else stays untouched
    existing.update(updated_fields)

    return {"message": "item partially updated successfully", "item": fake_db[item_id]}


















