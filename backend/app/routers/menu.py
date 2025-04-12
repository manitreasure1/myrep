from fastapi import APIRouter


menu_router = APIRouter()

@menu_router.get("/coffe")
async def get_coffees():
    return {'coffees ': ['', '']}