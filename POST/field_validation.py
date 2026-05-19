from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=50,
        title="Item name",
        description="Name of the item (2–50 chars)",
    )
    description: Optional[str] = Field(
        default=None,
        max_length=300,
    )
    price: float = Field(
        gt=0,
        description="Must be greater than 0",
    )
    discount: float = Field(
        default=0.0,
        ge=0.0,
        lt=1.0,
        description="Fraction off (0.0 to 0.99)",
    )
    quantity: int = Field(ge=1, le=10_000)
    sku: str = Field(
        pattern=r"^[A-Z]{3}-\d{4}$",
        description="Format: ABC-1234",
        examples=["MUG-0042", "PEN-1337"],
    )


@app.post("/items")
def create_item(item: Item):
    final_price = item.price * (1 - item.discount)
    return {
        "item": item,
        "final_price": round(final_price, 2),
    }













