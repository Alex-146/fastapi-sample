from fastapi import FastAPI
from db import ItemModel
import ItemController

app = FastAPI()

@app.get("/")
def home():
  return { "Cucumber": 146 }

@app.get("/redirect")
def redirect(page: str = None):
  return { "page": page }

@app.get("/items")
def allItems():
  return ItemController.allItems()

@app.get("/items/{id}")
def singleItem(id: str):
  return ItemController.singleItem(id)

@app.post("/items")
def addItem(body: ItemModel):
  return ItemController.addItem(body.value)

@app.put("/items/{id}")
def updateItem(id: str, body: ItemModel):
  return ItemController.updateItem(id, body.value)

@app.delete("/items/{id}")
def deleteItem(id: str):
  return ItemController.deleteItem(id)
