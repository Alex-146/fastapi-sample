from pydantic import BaseModel

class ItemModel(BaseModel):
  value: str

items = [
  { "id": "greenApple", "value": "🍏"},
  { "id": "redApple", "value": "🍎"}
]

def getItemById(id: str):
  return next((i for i in items if i["id"] == id), None)
