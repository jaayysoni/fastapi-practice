# DELETE/delete_validation.py

# The honest delete — checks if the user exists before attempting removal.
# If not found, raises a 404. No silent passes like delete_basic.

from fastapi import FastAPI, HTTPException

app = FastAPI()

fake_db = {
    1: "Alice",
    2: "Bob",
    3: "Charlie"
}


@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    # If the ID doesn't exist, stop here and tell the client clearly
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="User not found")

    # ID confirmed — safe to delete
    del fake_db[user_id]
    return {"message": f"User {user_id} has been deleted successfully"}