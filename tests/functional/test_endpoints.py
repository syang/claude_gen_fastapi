import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import Base, get_db, get_test_db

app.dependency_overrides[get_db] = get_test_db

client = TestClient(app)

def test_create_item():
    response = client.post(
        "/items/",
        json={"name": "Test Item", "description": "This is a test item"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Item"
    assert data["description"] == "This is a test item"
    assert "id" in data

def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_read_item():
    # First, create an item
    create_response = client.post(
        "/items/",
        json={"name": "Test Item 2", "description": "This is another test item"},
    )
    assert create_response.status_code == 200
    created_item = create_response.json()
    
    # Now, try to read the created item
    response = client.get(f"/items/{created_item['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Item 2"
    assert data["description"] == "This is another test item"

def test_read_non_existent_item():
    response = client.get("/items/9999")
    assert response.status_code == 404