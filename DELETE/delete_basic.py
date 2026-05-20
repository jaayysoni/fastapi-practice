#DELETE/delete_basic.py

from fastapi import FastAPI

app = FastAPI()

fake_db = {1: "Alice", 2: "Bob", 3: "Charlie"}

@app.delete("/users/{user_id}")
def delete_item(user_id: int):
    fake_db.pop(user_id, None)
    return {"message": f"Item{user_id} deleted succcessfully"}





















