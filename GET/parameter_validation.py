# GET/parameter_validation.py 
from fastapi import FastAPI, Query, Path

app = FastAPI()


@app.get("/items/")
def get_items(limit: int = Query(default=10, ge=1, le=100)):
    return {"limit": limit}
    
@app.get("/users/{user_id}")
def get_user(user_id: int = Path(..., gt=1)):
    return {"user_id": user_id}

@app.get("/products/")
def get_products(price: int = Query(default = 10,lt = 50)):
    return {"price": price}


@app.get("/orders/")
def get_orders(
    status: str = Query(...),
    page: int = Query(default=1, ge=1)):
    return {"status": status,"page": page}















