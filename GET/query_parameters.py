from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/count")
def count_char(text: str, char: str):
    if len(char) != 1:
        raise HTTPException(status_code=400, detail="Parameter 'char' must be a single character.")
    else:
        return {"character": char, "count": text.count(char)}




