from fastapi import FastAPI

from api import router as api
from common.config import config


app = FastAPI(title=config.PROJECT_NAME)
app.include_router(api)


@app.get("/health")
def health_check():
    return {"200 OK":"healthy"}