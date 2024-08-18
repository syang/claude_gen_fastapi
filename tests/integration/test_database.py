import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_test_db
from app.models.item import Item

@pytest.fixture(scope="module")
def test_db():
    db = next(get_test_db())
    try:
        yield db
    finally:
        db.close()

def test_create_item(test_db):
    new_item = Item(name="Test Item", description="This is a test item")
    test_db.add(new_item)
    test_db.commit()
    
    item = test_db.query(Item).filter(Item.name == "Test Item").first()
    assert item is not None
    assert item.name == "Test Item"
    assert item.description == "This is a test item"

def test_get_item(test_db):
    new_item = Item(name="Another Test Item", description="This is another test item")
    test_db.add(new_item)
    test_db.commit()
    
    item = test_db.query(Item).filter(Item.name == "Another Test Item").first()
    assert item is not None
    assert item.name == "Another Test Item"
    assert item.description == "This is another test item"