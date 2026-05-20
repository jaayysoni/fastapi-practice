#DELETE/delete_with_response.py

from fastapi import FastAPI, Response, status


app = FastAPI()


fake_db = {
    1: "Alice", 2: "Bob", 3: "charlie"
}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    fake_db.pop(user_id, None)

    return Response(status_code=status.HTTP_204_NO_CONTENT)

























