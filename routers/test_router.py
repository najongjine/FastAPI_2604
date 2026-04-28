from fastapi import APIRouter
from utils.common import CommonResponse

router = APIRouter(
    prefix="/test",
    tags=["test"]
)

@router.get("/")
def test_home():
    return {"message": "Test Router Home"}

@router.get("/info")
def test_info(name: str = "", age: int = 0):
    try:
        # 비즈니스 로직 처리
        result_data = {
            "name": name,
            "age": age,
            "message": f"안녕하세요 {name}님, 나이는 {age}세군요!"
        }
        
        return CommonResponse(success=True, data=result_data)
    except Exception as e:
        return CommonResponse(success=False, msg=str(e))
