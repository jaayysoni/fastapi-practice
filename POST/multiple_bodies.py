from typing import Optional
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()


# First model — describes the item being ordered
class Item(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    price: float = Field(gt=0)
    stock: int = Field(ge=0)


# Second model — describes the supplier providing the item
class Supplier(BaseModel):
    company: str = Field(min_length=2, max_length=100)
    contact_email: str = Field(pattern=r"^[\w\.-]+@[\w\.-]+\.\w{2,}$")
    rating: float = Field(ge=0.0, le=5.0)


# ── Route 1: Two models in one request ───────────────────────────────────────
# FastAPI automatically wraps each model under its parameter name as the key.
# So the client must send:
# {
#     "item": { "name": "Keyboard", "price": 999.0, "stock": 50 },
#     "supplier": { "company": "TechCorp", "contact_email": "a@b.com", "rating": 4.5 }
# }
@app.post("/items/with-supplier")
def create_item_with_supplier(item: Item, supplier: Supplier):
    return {
        "item": item,
        "supplier": supplier,
    }


# ── Route 2: Two models + a plain value ──────────────────────────────────────
# "importance" is just a plain int, not a model.
# We wrap it with Body() so FastAPI knows it belongs in the request body
# and not in the query parameters.
# Client sends:
# {
#     "item": { "name": "Mouse", "price": 499.0, "stock": 100 },
#     "supplier": { "company": "ClickCo", "contact_email": "x@y.com", "rating": 3.8 },
#     "importance": 5
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


# ── Route 3: Single model with embed=True ────────────────────────────────────
# Normally with one model FastAPI expects a flat body:
#   { "name": "...", "price": ..., "stock": ... }
# embed=True forces it to be wrapped under the key "item":
#   { "item": { "name": "...", "price": ..., "stock": ... } }
# Useful when you want consistent nested structure even with one model.
@app.post("/items/embedded")
def create_item_embedded(item: Item = Body(embed=True)):
    return {"item": item}


# ── Route 4: Second model is optional ────────────────────────────────────────
# The client can send just the item without a supplier.
# If supplier is not sent, it defaults to None and we handle it gracefully.
@app.post("/items/optional-supplier")
def create_item_optional_supplier(
    item: Item,
    supplier: Optional[Supplier] = None,
):
    if supplier:
        return {"item": item, "supplier": supplier}
    return {"item": item, "supplier": "not provided"}