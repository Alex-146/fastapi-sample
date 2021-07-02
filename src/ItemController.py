from datetime import datetime
import db

def allItems():
  return { "ok": True, "data": db.items }

def singleItem(id: str):
  item = db.getItemById(id)
  if item:
    return { "ok": True, "data": item }
  else:
    return { "ok": False }

def addItem(value: str):
  item = { "id": str(int(datetime.now().timestamp())), "value": value }
  return { "ok": True, "data": db.items + [item] }

def updateItem(id: str, value: str):
  item = db.getItemById(id)
  if item:
    updatedItem = { "id": id, "value": value }
    return { "ok": True, "data": list(filter(lambda i: i["id"] != id, db.items)) + [updatedItem] }
  else:
    return { "ok": False }

def deleteItem(id: str):
  item = db.getItemById(id)
  if item:
    return { "ok": True, "data": list(filter(lambda i: i["id"] != id, db.items)) }
  else:
    return { "ok": False }
