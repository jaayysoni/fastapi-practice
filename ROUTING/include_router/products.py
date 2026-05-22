from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_products():
    return ["product1", "product2"]

@router.get("/{id}")
def get_product_by_id(id: int):
    return {"id": id}













































