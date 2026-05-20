# DELETE/delete_multiple.py

# Bulk delete — one request, multiple IDs. Much better than calling DELETE 50 times.

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
    ids: List[int]  # client sends a list of IDs to delete


@app.delete("/users/bulk")
def delete_multiple(request: DeleteRequest):
    deleted = []
    not_found = []

    for user_id in request.ids:
        if user_id in fake_db:
            del fake_db[user_id]
            deleted.append(user_id)
        else:
            not_found.append(user_id)  # don't crash, just track it

    # clear split — what was deleted, what wasn't found
    return {
        "deleted": deleted,
        "not_found": not_found
    }



