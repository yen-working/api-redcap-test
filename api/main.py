from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
class Item(BaseModel):
    name: str

class RedCapDET(BaseModel):
    project_id: int
    username: str
    instrument: str
    record: int
    redcap_event_name: str
    redcap_data_access_group: str
    # [instrument]_complete: int
    redcap_repeat_instance: int
    redcap_repeat_instrument: str
    redcap_url: str
    project_url: str
    
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

@app.get("/allTests")
def get_tests():
    return tests

@app.get("/allItems")
def get_items():
    return items

@app.post('/testPost')
async def test(det: RedCapDET):
    tests.append(det)
    return tests
