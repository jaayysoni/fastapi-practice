#POST/nested_models.py 

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Address(BaseModel):
    city: str
    zip_code: str
    country: str

class User(BaseModel):
    name: str
    email: str
    address: Address

class Item(BaseModel):
    product_name: str
    price: float
    quantity: int

class Order(BaseModel):
    customer_name: str
    items: list[Item]
    shipping_address: Address

@app.post("/orders/")
def place_order(order: Order):
    total = sum(item.price * item.quantity for item in order.items)
    return {
        "customer": order.customer_name,
        "total_amount": total,
        "ship_to": order.shipping_address.city
    }






















































