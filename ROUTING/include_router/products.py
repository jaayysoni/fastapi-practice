# Concept APIRouter products resource
# What this covers defining product routes in a separate file using APIRouter
# Run uvicorn ROUTING.include_router.main:app --reload

from fastapi import APIRouter

# this router collects all product routes
# main.py will pick this up and register it with prefix /products
router = APIRouter()

# returns all products, in real app this would query the database
@router.get("/")
def get_products():
    return ["product1", "product2"]

# returns a single product by id, id comes from the URL path
@router.get("/{id}")
def get_product_by_id(id: int):
    return {"id": id}