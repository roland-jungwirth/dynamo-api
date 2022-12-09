from fastapi import Depends, FastAPI, HTTPException

from .routers import users
from .routers import clean

app = FastAPI()

app.include_router(users.router)
app.include_router(clean.router)

@app.get("/")
async def root(token: str = Depends(users.oauth2_scheme)  ):
    return {"message": "Welcome to the Dynamo API"}

