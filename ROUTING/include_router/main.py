from fastapi import FastAPI
from ROUTING.include_router.users import router as users_router

app = FastAPI()
app.include_router(users_router)


































