from fastapi import FastAPI
from app.api.v1 import router as v1_router
from server.core.config import config

app = FastAPI(title=config.PROJECT_NAME)

app.include_router(v1_router, prefix=config.API_V1_STR)

@app.get("/health")
def health_check():
    return {"200 OK":"healthy"}