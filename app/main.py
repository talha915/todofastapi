from fastapi import FastAPI
from api.routers import items

app = FastAPI()

# Include the item and user routers
app.include_router(items.router, prefix="/items", tags=["items"])
