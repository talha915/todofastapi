from typing import List, Optional
from api.models.item import Item

items = []

def get_items(skip: int = 0, limit: int = 10):
    return items[skip: skip+limit]

def get_item(item_id: int):
    specific_item = next((item for item in items if item["id"] == item_id), None)
    return specific_item

def create_item(item: Item)->dict:
    item_dict = item.dict()
    item_dict["id"] = len(items) + 1
    items.append(item)
    return item_dict