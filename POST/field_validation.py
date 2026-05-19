from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


# This is our "blueprint" for what a valid item looks like.
# Before any of your code runs, FastAPI checks every incoming
# request against these rules. Bad data gets rejected with a
# 422 error — your route function never even sees it.
class Item(BaseModel):

    # name must be at least 2 characters and at most 50.
    # title and description only show up in /docs — they help
    # whoever is reading your API understand what this field is for.
    name: str = Field(
        min_length=2,
        max_length=50,
        title="Item name",
        description="Name of the item (2–50 chars)",
    )

    # Optional means the client doesn't have to send this field.
    # If they don't send it, it defaults to None.
    # But if they DO send it, it can't be longer than 300 chars.
    description: Optional[str] = Field(
        default=None,
        max_length=300,
    )

    # gt=0 means "greater than 0" — so 0.01 is fine, but 0 or
    # negative numbers are rejected. You don't want free or
    # negative priced items in your store.
    price: float = Field(
        gt=0,
        description="Must be greater than 0",
    )

    # Discount is a fraction — 0.1 means 10% off, 0.5 means 50% off.
    # ge=0.0 means it can't be negative (no negative discounts).
    # lt=1.0 means it can't be 1.0 or above (you can't give 100% off).
    # default=0.0 means if the client doesn't send it, assume no discount.
    discount: float = Field(
        default=0.0,
        ge=0.0,
        lt=1.0,
        description="Fraction off (0.0 to 0.99)",
    )

    # quantity must be at least 1 (you can't order 0 items)
    # and at most 10,000 (reasonable upper limit for a single order).
    quantity: int = Field(ge=1, le=10_000)

    # SKU is a product code that must follow a strict company format.
    # The pattern r"^[A-Z]{3}-\d{4}$" means:
    #   - exactly 3 uppercase letters
    #   - followed by a hyphen
    #   - followed by exactly 4 digits
    # So "MUG-0042" passes, but "mug-42" or "MUGGG-1" fails.
    # examples only shows up in /docs as sample values.
    sku: str = Field(
        pattern=r"^[A-Z]{3}-\d{4}$",
        description="Format: ABC-1234",
        examples=["MUG-0042", "PEN-1337"],
    )


@app.post("/items")
def create_item(item: Item):
    # By the time we reach this line, all fields are already validated.
    # We don't need any manual if/else checks here.

    # Calculate the final price after applying the discount.
    # Example: price=100, discount=0.1 → final_price = 100 * 0.9 = 90.0
    final_price = item.price * (1 - item.discount)

    return {
        "item": item,
        "final_price": round(final_price, 2),  # round to 2 decimal places
    }




















