from fastapi import FastAPI
from app.model.model import Item
app = FastAPI()
db = []

@app.get("/")
def read_root():
    return {"message": "Hello, GitHub Actions!"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/demo")
async def demo_endpoint():
    return {"message": "This is the demo endpoint!"}

@app.post("/add_item")
async def add_item(item: Item):
    db.append(item.item)
    return {"message": "Item added successfully!"}

@app.get("/items")
async def get_items():
    return {"items": db}