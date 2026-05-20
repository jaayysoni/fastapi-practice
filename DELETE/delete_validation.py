#DELETE/delete_validation.py
from fastapi import FastAPI, HTTPException


app = FastAPI()

fake_db = {
    1: "Alice", 
    2: "Bob",
    3: "charlie"
}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="User not Found")
    
    del fake_db[user_id]
    return {"message": f"User with id {user_id} has been deleted"}


















