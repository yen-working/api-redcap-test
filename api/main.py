from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
class Item(BaseModel):
    name: str
    
app = FastAPI()
items = []
tests = []

@app.post("/items/")
async def create_item(item: Item):
    items.append(item)
    return item

@app.get("/all")
def get_items():
    return items

@app.post('/test')
async def test():
    item = Item(name=datetime.now())
    items.append(item)
    return item

@app.post('/')
def home():
    return "Hello, Woooo"