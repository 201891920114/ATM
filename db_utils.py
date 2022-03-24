from replit import db
import json

def save_object(key, val):
  db[key] = json.dumps(val)

def get_object(key, default_value=""):
  if not key in db.keys():
    save_object(key, default_value)
    return default_value
  return json.loads(db[key])

def clear_list(key):
  del db[key]
  save_object(key, [])

def remove_from_list(key, val):
  if key in db.keys():
    items = get_object(key)
    items.remove(val)
    save_object(key, items)
    return items
  return None

def add_to_list(key, val):
  items = get_object(key)
  if items is None:
    items = []
    save_object(key, items)
  if val not in items:
    items.append(val)
    save_object(key, items)
  return items
