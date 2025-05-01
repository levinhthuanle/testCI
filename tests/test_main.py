from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, GitHub Actions!"}

def test_say_hello():
    response = client.get("/hello/ChatGPT")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, ChatGPT!"}
    
    response = client.get("/hello/World")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}
    
def test_demo_endpoint():
    response = client.get("/demo")
    assert response.status_code == 200
    assert response.json() == {"message": "This is the demo endpoint!"}

def test_add_item():
    response = client.post("/add_item", json={"item": "apple"})
    assert response.status_code == 200
    assert response.json() == {"message": "Item added successfully!"}
    
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == {"items": ["apple"]}
    
    response = client.post("/add_item", json={"item": "banana"})
    assert response.status_code == 200
    assert response.json() == {"message": "Item added successfully!"}
    
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == {"items": ["apple", "banana"]}