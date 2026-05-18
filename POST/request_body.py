# POST/request_body.py
# This file shows how to accept JSON data in a POST request using FastAPI and Pydantic.
# Real world use case is any time you are creating something like a user or an order
# the client sends data in the request body and your API receives it here.

from fastapi import FastAPI
from pydantic import BaseModel  # BaseModel is what gives our class validation superpowers

app = FastAPI()


# This is our data model. It defines exactly what the incoming JSON should look like.
# If the client sends wrong types or misses a field Pydantic rejects it automatically.
# No manual validation needed. This class handles all of that.
class User(BaseModel):
    name: str   # must be a string
    email: str  # must be a string
    age: int    # must be an integer. sending "hello" here will give a 422 error


# POST /users/ creates a new user
# FastAPI reads the request body and validates it against the User model
# and only calls this function if everything is correct.
# If something is wrong like a missing field or wrong type it returns 422 before even reaching here.
@app.post("/users/")
def create_user(user: User):
    # at this point user.name user.email and user.age are all guaranteed to be valid
    return {
        "message": "User created successfully",
        "user": user  # FastAPI automatically converts the Pydantic object to JSON
    }