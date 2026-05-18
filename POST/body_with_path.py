# POST/body_with_path.py
# This file shows how to combine a path parameter and a request body in a single endpoint.
# Real world use case is when you are creating something that belongs to a specific resource
# like adding an item for a particular user. The user id comes from the URL
# and the item details come from the request body.

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# This defines what an item looks like when the client sends it in the request body
# price is a float so 100 will automatically become 100.0
# in_stock is a bool so the client sends true or false
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool


# POST /users/{user_id}/items/ creates an item for a specific user
# FastAPI automatically knows that user_id comes from the URL
# and item comes from the request body because Item is a Pydantic model
# you do not need to write any parsing logic FastAPI handles it
@app.post("/users/{user_id}/items/")
def create_item_for_user(user_id: int, item: Item):
    # user_id is guaranteed to be an integer because it is type hinted as int
    # item is guaranteed to have valid name price and in_stock because Pydantic validated it
    return {
        "message": "Item created successfully",
        "user_id": user_id,
        "item": item
    }









