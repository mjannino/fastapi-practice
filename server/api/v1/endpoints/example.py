from fastapi import APIRouter

from app.crud.user import update_user
from server.models.example import ExampleEntity

router = APIRouter()

@router.get("/example", response_model=ExampleEntity, tags=["entities"])
def get_example(): # async def -- only if you are awaiting from db
    return ExampleEntity(
        name="Bint", 
        mail="bint@bint.com",
        bio=None,
        website="bint.com",
        additional_field="woa!")