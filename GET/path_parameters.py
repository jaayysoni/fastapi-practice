# GET/path_parameters.py
from fastapi import FastAPI, HTTPException

app = FastAPI()

fake_db = {
    1: {"name": "Jay", "role": "engineer"},
    2: {"name": "Alex", "role": "designer"},
}


@app.get("/users/{user_id}", responses = {404 : {"description": "user not found"}})
def read_user(user_id: int):
    if user_id not in fake_db:
        raise HTTPException(status_code = 404, detail = "User not found")
    return fake_db[user_id]



