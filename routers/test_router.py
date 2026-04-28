from fastapi import APIRouter

router = APIRouter(
    prefix="/test",
    tags=["test"]
)

@router.get("/")
def test_home():
    return {"message": "Test Router Home"}

@router.get("/info")
def test_info():
    return {"info": "This is a test router"}
