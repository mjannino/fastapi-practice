from fastapi import APIRouter

from common.config import config
# maybe enforce a name convention to avoid aliasing?
from api.endpoints.run import (
    run_v1, 
    run_v2
)
from api.endpoints.walk import (
    walk_v1, 
    walk_v2
)

router = APIRouter()

router.include_router(run_v1, prefix=config.API_V1_STR)
router.include_router(run_v2, prefix=config.API_V2_STR)
router.include_router(walk_v1, prefix=config.API_V1_STR)
router.include_router(walk_v2, prefix=config.API_V2_STR)
