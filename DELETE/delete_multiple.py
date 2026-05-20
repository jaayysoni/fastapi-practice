#DELETE/delete_multiple.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()

fake_db = {
    1: "Alice",
    2: "Bob",
    3: "Charlie",
    4: "Diana",
    5: "Eve"

}

class DeleteRequest(BaseModel):
    ids: List[int]

@app.delete("/users/bulk")
def delete_multiple(request: DeleteRequest):
    deleted = []
    not_found = []

    for user_id in request.ids:
        if user_id in fake_db:
            del fake_db[user_id]
            deleted.append(user_id)
        else:
            not_found.append(user_id)

    return {
        "deleted": deleted,
        "not_found": not_found
    }






















