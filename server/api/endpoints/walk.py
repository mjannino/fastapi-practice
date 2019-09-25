from fastapi import APIRouter

from server.schemas.example import ExampleEntityV1, ExampleEntityV2
from server.common.config import config

walk_v1 = APIRouter()
walk_v2 = APIRouter()


@walk_v1.get("/walk", tags=["walk"])
def get_walk_v1():
    return {"walkv1":"wow"}


@walk_v2.get("/walk", tags=["walk"])
def get_walk_v2():
    return {"walkv2":"wow"}