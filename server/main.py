from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
def check_the_thing():
    return {"Test": "The thing"}
