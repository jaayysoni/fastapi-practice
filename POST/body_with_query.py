#POST/body_with_query.py

from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.post("/items/{item_id}")
def update_item(
    item_id: int,
    item: Item,
    notify: bool = False,
):
    result = {
        "item_id": item_id,
        "item": item,
        "item_price": item.price,
    }

    if item.tax:
        result["price_with_tax"] = item.price + item.tax

    if notify:
        result["message"] = "ware House is been notified"
    else:
        result["message"] = "item updated scilently"\
        

    return result





# To run the app, use the command: uvicorn POST.body_with_query:app --reload

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class ValidationItem(BaseModel):
    name: str = Field(
        min_length=3,
        max_length=50,
        title="Item Name",
        description="Name Must be between 3 and 50 characters",
    )

    secription: Optional[str] = Field(
        default=None,
        max_length=300,
        title="Item Description",
    )
    price: float = Field(
        gt = 0,
        title = "Item Price",
        description = "Price must be greater than zero",
    )
    discount: Optional[float] = Field(
        defualt = 0.0,
        ge= 0,
        le=100,
        description = "Discount percentage, 0 to 100 "
    )

@app.post("/items/{item_id}")
def body_with_query(
    item_id: int,
    item: Item,
    notify: bool = False,
):
    result = {
        "item_id": item_id,
        "item": item,
        "item_price": item.price,
    }

    if item.tax:
        result["price_with_tax"] = item.price + item.tax

    if notify:
        result["message"] = "ware House is been notified"
    else:
        result["message"] = "item updated scilently"

    return result


@app.post("/validation-items/")
def field_validation(item: ValidationItem):
    final_price = item.price - (item.price * item.discount / 100)
    return {
        "name": item.name,
        "original_price": item.price,
        "discount": item.discount,
        "final_price": final_price,
    }
























