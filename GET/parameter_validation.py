# GET/parameter_validation.py
from fastapi import FastAPI, Query, Path
from typing import List
from enum import Enum

app = FastAPI()


# Query param with range validation
# ge=1 means minimum 1, le=100 means maximum 100
# try: /items/?limit=5  or  /items/?limit=200 (fails)
@app.get("/items/")
def get_items(limit: int = Query(default=10, ge=1, le=100)):
    return {"limit": limit}


# Path param with validation
# gt=1 means user_id must be greater than 1
# the value comes from the URL itself, not a query string
# try: /users/5  or  /users/0 (fails)
@app.get("/users/{user_id}")
def get_user(user_id: int = Path(..., gt=1)):
    return {"user_id": user_id}


# Query param with upper limit only
# lt=50 means price must be less than 50
# try: /products/?price=30  or  /products/?price=60 (fails)
@app.get("/products/")
def get_products(price: int = Query(default=10, lt=50)):
    return {"price": price}


# Multiple query params in one request
# status is required (no default), page is optional
# try: /orders/legacy/?status=shipped&page=2
@app.get("/orders/legacy/")
def get_orders_legacy(
    status: str = Query(...),
    page: int = Query(default=1, ge=1)):
    return {"status": status, "page": page}


# Query param with metadata — title and description show up in /docs
# useful when you want the Swagger UI to explain what a param does
# try: /reports/?year=2023
@app.get("/reports/")
def get_reports(
    year: int = Query(
        default=2025,
        title="Report Year",
        description="Fiscal year of the report, must be between 2000 and 2100",
        ge=2000,
        le=2100
    )
):
    return {"year": year}


# Alias — the client sends "item-name" but FastAPI maps it to "name"
# useful when the param name you want in Python isn't valid as a URL key
# try: /products/search/?item-name=keyboard
@app.get("/products/search/")
def search_products(
    name: str = Query(..., alias="item-name")
):
    return {"name": name}


# Deprecated param — limit still works but shows as struck-through in /docs
# use this when you're phasing out a param but can't remove it yet
# try: /legacy/items/?limit=5&page_size=20
@app.get("/legacy/items/")
def legacy_items(
    limit: int = Query(default=10, deprecated=True),
    page_size: int = Query(default=10)
):
    return {"limit": limit, "page_size": page_size}


# List param — same key repeated in the URL gives you a Python list
# useful for filtering by multiple values in one request
# try: /items/tags/?tag=python&tag=fastapi&tag=redis
@app.get("/items/tags/")
def get_items_by_tag(tag: List[str] = Query(default=[])):
    return {"tag": tag}


# Required list param — must send at least one value
# try: /search/?ids=1&ids=2&ids=3  or  /search/ (fails)
@app.get("/search/")
def search(ids: List[int] = Query(...)):
    return {"ids": ids}


# List param with length limits — min 1 value, max 10 values
# try: /batch/?ids=1&ids=2  or send 11 values (fails)
@app.get("/batch/")
def batch(ids: List[int] = Query(default=[], min_length=1, max_length=10)):
    return {"ids": ids, "count": len(ids)}


# Enum — only these exact values are accepted, anything else gets a 422
# inherit from both str and Enum so FastAPI can serialize it to JSON
class OrderStatus(str, Enum):
    pending   = "pending"
    shipped   = "shipped"
    delivered = "delivered"
    cancelled = "cancelled"

class SortOrder(str, Enum):
    asc  = "asc"
    desc = "desc"


# Enum params in action — status and sort are both locked to their enum values
# Swagger shows a dropdown automatically for each enum param
# try: /orders/?status=shipped&sort=asc  or  /orders/?status=flying (fails)
@app.get("/orders/")
def get_orders_enum(
    status: OrderStatus = Query(default=OrderStatus.pending),
    sort: SortOrder = Query(default=SortOrder.desc)
):
    return {"status": status, "sort": sort}
























