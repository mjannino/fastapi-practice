from fastapi import APIRouter

from schemas.example import ExampleEntityV1, ExampleEntityV2
from common.config import config

run_v1 = APIRouter()
run_v2 = APIRouter()


@run_v1.get("/run", response_model=ExampleEntityV1, tags=["run"])
def get_run_information_v1():
    return ExampleEntityV1(
        name="Sonic the Hedgehog", 
        email="runfast@sonic.com",
        bio=None,
        website="http://www.gottagofast.com",
        additional_field="woa! speedy!")


@run_v2.get("/run", response_model=ExampleEntityV2, tags=["run"])
def get_run_information_v2():
    return ExampleEntityV1(
        name="Sonic the Hedgehog", 
        email="runfast@sonic.com",
        bio=None,
        website="http://www.gottagofast.com",
        breaking_change_field="brand spankin' new field")