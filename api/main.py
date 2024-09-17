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
    # tests.append(el)
    # el = el + 1
    item = Item()
    item.name = datetime.now()
    items.append(item)
    return item