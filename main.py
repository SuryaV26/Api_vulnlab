from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def root():
    return "hello world"

@app.get("/add/{n1}")
def add(n1: int):
    return {"result": n1*n1}