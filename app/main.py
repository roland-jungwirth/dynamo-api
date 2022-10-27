from fastapi import Depends, FastAPI

from .routers import clean

app = FastAPI()

app.include_router(clean.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Dynamo API"}

