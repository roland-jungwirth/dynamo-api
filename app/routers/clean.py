from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/clean",
    tags=["clean"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_items():
    return {"message": "Just a test"}
