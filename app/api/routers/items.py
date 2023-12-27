from fastapi import APIRouter, HTTPException
from api import crud
from api.models import item as models
from typing import List

router = APIRouter()

@router.post("/add", response_model=models.Item)
def create_item(item: models.Item):
    """Create a new item."""
    return crud.create_item(item)

@router.get("/", response_model=List[models.Item])
async def get_all_items(skip: int=0, limit: int=10):
    return crud.get_items(skip=skip, limit=limit)    