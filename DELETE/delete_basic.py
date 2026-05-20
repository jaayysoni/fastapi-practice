# DELETE/delete_basic.py

# The most basic form of DELETE — no checks, no complaints.
# Just "remove it if it's there, ignore it if it's not."
# This is fine for low-stakes stuff like cart items or draft posts.

from fastapi import FastAPI

app = FastAPI()

# Simulating a database with a simple dictionary
fake_db = {1: "Alice", 2: "Bob", 3: "Charlie"}


@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    # pop(user_id, None) is the key here —
    # if user_id exists, it gets deleted.
    # if it doesn't (like user 99), it just moves on quietly — no crash, no error.
    # That's why even DELETE /users/99 returns 200. It's not lying, it's just... unbothered.
    fake_db.pop(user_id, None)

    return {"message": f"User {user_id} deleted successfully"}