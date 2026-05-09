from fastapi import FastAPI, HTTPException, Query

app = FastAPI()

@app.get("/count")
def count_char(text: str, char: str):
    if len(char) != 1:
        raise HTTPException(status_code=400, detail="Parameter 'char' must be a single character.")
    return {"character": char, "count": text.count(char)}


@app.get("/twosum")
def two_sum(nums: str, target: int):
    nums = [int(x) for x in nums.split(",")]
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return {"index1": seen[diff], "index2": i}
        seen[num] = i
    raise HTTPException(status_code=404, detail="No two sum solution found.")