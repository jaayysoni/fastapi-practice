# Concept APIRouter users resource
# What this covers defining user routes in a separate file using APIRouter
# Run uvicorn ROUTING.include_router.main:app --reload

from fastapi import APIRouter

# this router collects all user routes
# main.py will pick this up and register it with prefix /users
router = APIRouter()

# returns all users, in real app this would query the database
@router.get("/")
def get_users():
    return ["user1", "user2"]