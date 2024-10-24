from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
class Item(BaseModel):
    name: str
    
app = FastAPI()
items = []
tests = []

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/items/")
async def create_item(item: Item):
    items.append(item)
    return item

@app.get("/all")
def get_items():
    return items

@app.post('/testPost')
async def test():
    return {"message": "POST request success"}
