# GET/parameter_validation.py 
from fastapi import FastAPI, Query, Path
from typing import List

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

@app.get("/reports/")
def get_reports(
    year: int = Query(
        default = 2025,
        title = "Report Year",
        description = "Fiscal Year of the report, must be betweeb 2010 to 2100",
        ge = 2000,
        le = 2100
    )
):
    return {"year": year}

@app.get("/products/search/")
def search_products(
    name: str = Query(...,alias= "item-name")
):
    return {"name": name}

@app.get("/legacy/items/")
def legacy_items(
    limit: int = Query(default=10, deprecated=True),
    page_size: int = Query(default=10)
):
    return {"limit": limit, "page_size": page_size}


@app.get("/items/")
def get_items(tag: List[str] = Query(default = [])):
    return {"tag": tag}

@app.get("/search/")
def search(ids: List[int] = Query(...)):
    return {"ids": ids}

@app.get("/batch/")
def batch(ids: List[int] = Query(default = [], min_lenght = 1, max_lenght = 10)):
    return {"ids": ids, "count": len(ids)}


    















#7 List Params    ⏳
#8 Enum Params    ⏳














