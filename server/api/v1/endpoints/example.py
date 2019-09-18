from fastapi import APIRouter

from server.models.example import ExampleEntity

router = APIRouter()

@router.get("/example", response_model=ExampleEntity, tags=["entities"])
def get_example(): # async def -- only if you are awaiting from db
    return ExampleEntity(
        name="Bint", 
        email="bint@bint.com",
        bio=None,
        website="http://www.bint.com",
        additional_field="woa!")