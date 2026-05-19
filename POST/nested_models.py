# POST/nested_models.py
# Topic: Nested Models in FastAPI
#
# Nested models = a Pydantic model used as a field inside another Pydantic model.
# This lets you represent structured, hierarchical JSON data (objects inside objects).
#
# Real-world use cases:
#   - User has an Address
#   - Order has a list of Items + a shipping Address
#   - Product has Dimensions, Dimensions has a Unit
#
# Key benefits:
#   - FastAPI validates every level of nesting automatically
#   - Access nested data with simple dot notation (e.g. order.shipping_address.city)
#   - Models can be reused across multiple parent models (e.g. Address used in both User and Order)
#   - Auto-generates nested JSON schema in /docs (Swagger UI)

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# --- Reusable nested model ---
# Address is a standalone model that can be embedded inside any other model.
# Reused in both User and Order below.
class Address(BaseModel):
    city: str
    zip_code: str
    country: str


# --- Single nested object example ---
# User contains one Address object as a field.
# Expected JSON:
# {
#   "name": "Jay",
#   "email": "jay@example.com",
#   "address": { "city": "Bhopal", "zip_code": "462001", "country": "India" }
# }
class User(BaseModel):
    name: str
    email: str
    address: Address        # single nested model


# --- Nested model used inside a list ---
# Item represents one product in an order.
# Used as list[Item] inside Order below.
class Item(BaseModel):
    product_name: str
    price: float
    quantity: int


# --- Complex nested model: list of objects + nested object ---
# Order contains:
#   - items: a list of Item objects  (list of nested models)
#   - shipping_address: an Address object  (single nested model, reused from above)
#
# Expected JSON:
# {
#   "customer_name": "Jay Soni",
#   "items": [
#     { "product_name": "Keyboard", "price": 2999.99, "quantity": 2 },
#     { "product_name": "USB Hub",  "price": 899.50,  "quantity": 1 }
#   ],
#   "shipping_address": { "city": "Bhopal", "zip_code": "462001", "country": "India" }
# }
class Order(BaseModel):
    customer_name: str
    items: list[Item]           # list of nested models — FastAPI validates each Item
    shipping_address: Address   # reusing the Address model


# --- Route ---
# POST /orders/
# Accepts a fully nested Order body, computes the total, and returns a summary.
@app.post("/orders/")
def place_order(order: Order):
    # Iterate over list[Item] — each `item` is a fully validated Item object
    # Access fields with dot notation: item.price, item.quantity
    total = sum(item.price * item.quantity for item in order.items)

    return {
        "customer": order.customer_name,            # top-level field
        "total_amount": total,                      # computed from nested list
        "ship_to": order.shipping_address.city      # dot notation into nested object
    }
















