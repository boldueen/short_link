from fastapi import APIRouter

router = APIRouter()

@router.get('/', status_code=200)
async def testssss():
    return {"socials":"correct"}