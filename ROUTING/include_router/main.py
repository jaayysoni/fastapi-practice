from fastapi import FastAPI
from ROUTING.include_router.users import router as users_router
from ROUTING.include_router.products import router as products_router

app = FastAPI()
app.include_router(users_router, prefix="/users",tags = ["Users"] )
app.include_router(products_router, prefix="/products", tags = ["Products"])




































