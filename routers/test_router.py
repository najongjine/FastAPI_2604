from fastapi import APIRouter

router = APIRouter(
    prefix="/test",
    tags=["test"]
)

@router.get("/")
def test_home():
    return {"message": "Test Router Home"}

@router.get("/info")
def test_info(name: str="", age: int = 0):
    return {
        "name": name,
        "age": age,
        "message": f"안녕하세요 {name}님, 나이는 {age}세군요!"
    }
