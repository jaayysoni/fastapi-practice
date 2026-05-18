# POST/body_with_query.py
# This file covers two POST concepts:
# 1. Sending a request body along with path and query parameters
# 2. Validating fields using Field() from pydantic

from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()


# ─── CONCEPT 1: BODY WITH PATH + QUERY ────────────────────────────────────────
#
# Sometimes your endpoint needs three things at once:
#   - path param  → tells you WHICH item (from the URL)
#   - request body → tells you WHAT data (from JSON)
#   - query param  → tells you HOW to behave (from ?notify=true)
#
# FastAPI is smart enough to read all three sources automatically.
# You don't configure anything — it just figures it out by type.

class Item(BaseModel):
    name: str
    description: Optional[str] = None  # optional, defaults to None if not sent
    price: float
    tax: Optional[float] = None         # optional tax, used to calculate final price


# path:  /items/42         → item_id = 42
# body:  { "name": ... }   → item = Item(...)
# query: ?notify=true      → notify = True
@app.post("/items/{item_id}")
def body_with_query(
    item_id: int,        # from URL path
    item: Item,          # from request body (JSON)
    notify: bool = False # from query string, default is False
):
    result = {
        "item_id": item_id,
        "item": item,
        "item_price": item.price,
    }

    # only add tax field to response if tax was actually sent
    if item.tax:
        result["price_with_tax"] = item.price + item.tax

    # query param controls behavior — same endpoint, different outcome
    if notify:
        result["message"] = "Warehouse has been notified"
    else:
        result["message"] = "Item updated silently"

    return result


# ─── CONCEPT 2: FIELD VALIDATION ──────────────────────────────────────────────
#
# By default Pydantic only checks types (str, float, int).
# Field() lets you go further — enforce rules like:
#   - string length limits
#   - number ranges (price can't be 0 or negative)
#   - custom descriptions that show up in Swagger docs
#
# The best part: if validation fails, FastAPI auto-returns a 422 error
# with the exact field, rule, and value that failed. Your function never runs.

class ValidationItem(BaseModel):
    name: str = Field(
        min_length=3,   # "AB" would be rejected
        max_length=50,  # very long names get rejected too
        title="Item Name",
        description="Name must be between 3 and 50 characters"
    )
    description: Optional[str] = Field(
        default=None,
        max_length=300,  # cap description length
        title="Item Description"
    )
    price: float = Field(
        gt=0,  # gt = greater than, so price=0 is rejected, must be > 0
        title="Item Price",
        description="Price must be greater than zero"
    )
    discount: Optional[float] = Field(
        default=0.0,
        ge=0,    # ge = greater than or equal, so 0% discount is allowed
        le=100,  # le = less than or equal, so 150% discount is rejected
        description="Discount percentage, between 0 and 100"
    )


@app.post("/validation-items/")
def field_validation(item: ValidationItem):
    # this code only runs if ALL field rules passed
    # if anything failed, FastAPI already sent back a 422
    final_price = item.price - (item.price * item.discount / 100)
    return {
        "name": item.name,
        "original_price": item.price,
        "discount_percent": item.discount,
        "final_price": round(final_price, 2)  # round to 2 decimal places
    }

