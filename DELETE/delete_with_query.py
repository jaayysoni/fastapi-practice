#DELETE/delete_with_query.py

from fastapi import FastAPI


app = FastAPI()

fake_db = {
    1: {"name": "Alice", "deleted": False},
    2: {"name": "Bob", "deleted": False},
    3: {"name": "Charlie", "deleted": False},
}

@app.delete("/items/{item_id}")
def delete_item(item_id: int, permanent: bool = False):
    if item_id not in fake_db:
        return {"error": "item not found"}
    
    if permanent:
        del fake_db[item_id]
        return {"message": f"Item {item_id} permanently deleted"}
    else:
        fake_db[item_id]["deleted"] = True
        return {"message": f"user{item_id} softly deleted (recoverable)" }

























