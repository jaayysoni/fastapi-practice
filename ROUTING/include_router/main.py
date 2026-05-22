# Concept: include_router
# What this covers: splitting routes into separate files and registering them in main app
# Run: uvicorn ROUTING.include_router.main:app --reload

from fastapi import FastAPI
from ROUTING.include_router.users import router as users_router
from ROUTING.include_router.products import router as products_router

app = FastAPI()

# prefix adds /users to every route in users_router
# tags groups them under "Users" section in /docs
app.include_router(users_router, prefix="/users", tags=["Users"])

# prefix adds /products to every route in products_router
# tags groups them under "Products" section in /docs
app.include_router(products_router, prefix="/products", tags=["Products"])