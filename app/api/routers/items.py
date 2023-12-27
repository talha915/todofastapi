from fastapi import APIRouter, HTTPException
from api import crud
from api.models import item as models

router = APIRouter()

@router.post("/add", response_model=models.Item)
def create_item(item: models.Item):
    """Create a new item."""
    return crud.create_item(item)