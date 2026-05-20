# DELETE/delete_with_query.py

# Soft delete vs Hard delete — controlled by ?permanent=true query param.
# Default is soft delete — safe, recoverable. Think Gmail's Trash.
# Hard delete only when explicitly requested — gone forever.

from fastapi import FastAPI

app = FastAPI()

# Each user has a "deleted" flag — soft delete just flips this to True
fake_db = {
    1: {"name": "Alice", "deleted": False},
    2: {"name": "Bob", "deleted": False},
    3: {"name": "Charlie", "deleted": False},
}


@app.delete("/items/{item_id}")
def delete_item(item_id: int, permanent: bool = False):

    if item_id not in fake_db:
        return {"error": "Item not found"}

    if permanent:
        # Hard delete — record is gone, no coming back
        del fake_db[item_id]
        return {"message": f"Item {item_id} permanently deleted"}
    else:
        # Soft delete — data stays, just marked as deleted
        fake_db[item_id]["deleted"] = True
        return {"message": f"Item {item_id} soft deleted (recoverable)"}