# DELETE/delete_with_response.py

# Same logic as delete_basic — but now we return 204 instead of 200.
# 204 = "Done. Nothing to send back." — the honest response for a DELETE.

from fastapi import FastAPI, Response, status

app = FastAPI()

fake_db = {1: "Alice", 2: "Bob", 3: "Charlie"}


@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):

    fake_db.pop(user_id, None)  # silently handles missing IDs like 99

    # 204 can't have a body — HTTP spec forbids it. FastAPI respects that.
    return Response(status_code=status.HTTP_204_NO_CONTENT)


