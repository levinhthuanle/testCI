from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, GitHub Actions!"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/demo")
async def demo_endpoint():
    return {"message": "This is the demo endpoint!"}
    
@app.get("/goodbye/{name}")
async def say_goodbye(name: str):
    return {"message": f"Goodbye, {name}!"}
