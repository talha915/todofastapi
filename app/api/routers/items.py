from fastapi import APIRouter, HTTPException
from api import crud
from api.models import item as models
from typing import List

router = APIRouter()

@router.get("/", response_model=List[models.Item])
async def get_all_items(skip: int=0, limit: int=10):
    return crud.get_items(skip=skip, limit=limit)   

@router.post("/add", response_model=models.Item)
def create_item(item: models.Item):
    """Create a new item."""
    return crud.create_item(item)

@router.get("/{item_id}", response_model=models.Item)
async def get_selected_item(item_id: int) -> dict:
    item = crud.get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item         