from typing import Optional
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()


# Blueprint for an item — defines what a valid item looks like.
# All fields are validated before your route function runs.
class Item(BaseModel):
    # name must be between 2 and 50 characters
    name: str = Field(min_length=2, max_length=50)
    # price must be greater than 0 — no free or negative priced items
    price: float = Field(gt=0)
    # stock can be 0 (out of stock is valid) but can't be negative
    stock: int = Field(ge=0)


# Blueprint for a supplier — who is providing the item.
class Supplier(BaseModel):
    # company name must be between 2 and 100 characters
    company: str = Field(min_length=2, max_length=100)
    # email must match a valid email format like jay@gmail.com
    # the pattern checks for: something@something.something
    contact_email: str = Field(pattern=r"^[\w\.-]+@[\w\.-]+\.\w{2,}$")
    # rating is between 0.0 and 5.0 — like a star rating
    rating: float = Field(ge=0.0, le=5.0)


# ── Route 1: Two models in one request ───────────────────────────────────────
# When you have two model parameters, FastAPI automatically expects
# the client to wrap each one under its parameter name as a key.
# So the client must send:
# {
#     "item": { "name": "Keyboard", "price": 999.0, "stock": 50 },
#     "supplier": { "company": "TechCorp", "contact_email": "a@b.com", "rating": 4.5 }
# }
# Both models are validated independently — if either one fails, the
# whole request is rejected with a 422.
@app.post("/items/with-supplier")
def create_item_with_supplier(item: Item, supplier: Supplier):
    return {
        "item": item,
        "supplier": supplier,
    }


# ── Route 2: Two models + a plain value in the body ──────────────────────────
# "importance" is just a plain int, not a Pydantic model.
# We wrap it with Body() to tell FastAPI it lives in the request body.
# Without Body(), FastAPI would look for it as a query parameter
# in the URL like /items/with-importance?importance=5 — which is wrong.
# Client sends:
# {
#     "item": { ... },
#     "supplier": { ... },
#     "importance": 5        ← must be between 1 and 10
# }
@app.post("/items/with-importance")
def create_item_with_importance(
    item: Item,
    supplier: Supplier,
    importance: int = Body(ge=1, le=10),
):
    return {
        "item": item,
        "supplier": supplier,
        "importance": importance,
    }


# ── Route 3: Single model forced into a key with embed=True ──────────────────
# Normally with just one model, FastAPI expects a flat body:
#   { "name": "Keyboard", "price": 999.0, "stock": 50 }
# But with embed=True it expects the model wrapped under the key "item":
#   { "item": { "name": "Keyboard", "price": 999.0, "stock": 50 } }
# Useful when you want a consistent nested structure even with one model.
@app.post("/items/embedded")
def create_item_embedded(item: Item = Body(embed=True)):
    return {"item": item}


# ── Route 4: Second model is completely optional ──────────────────────────────
# The client can send just the item without a supplier and it will still work.
# If supplier is not sent, it defaults to None.
# We then handle both cases — with and without supplier — in the function body.
# With supplier:    returns both item and supplier
# Without supplier: returns item and a message saying supplier was not provided
@app.post("/items/optional-supplier")
def create_item_optional_supplier(
    item: Item,
    supplier: Optional[Supplier] = None,
):
    if supplier:
        return {"item": item, "supplier": supplier}
    return {"item": item, "supplier": "not provided"}