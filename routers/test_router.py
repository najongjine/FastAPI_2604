from fastapi import APIRouter
from pydantic import BaseModel
from utils.common import CommonResponse

router = APIRouter(
    prefix="/test",
    tags=["test"]
)

class TestPostRequest(BaseModel):
    username: str = ""
    password: str = ""

@router.get("/")
def test_home():
    try:
        return CommonResponse(success=True)
    except Exception as e:
        return CommonResponse(success=False, msg=str(e))

@router.get("/info")
def test_info(name: str = "", age: int = 0):
    try:
        # 비즈니스 로직 처리
        data = {
            "name": name,
            "age": age
        }
        return CommonResponse(success=True, data=data)
    except Exception as e:
        return CommonResponse(success=False, msg=str(e))

@router.get("/mytest")
def mytest(username: str = "", password: str=""):
    try:
        # 비즈니스 로직 처리
        data = {
            "username": username,
            "password": password
        }
        return CommonResponse(success=True, data=data)
    except Exception as e:
        return CommonResponse(success=False, msg=str(e))

@router.post("/mytest")
def post_mytest(request: TestPostRequest):
    try:
        # business logic
        data = {
            "username": request.username,
            "password": request.password
        }
        return CommonResponse(success=True, data=data)
    except Exception as e:
        return CommonResponse(success=False, msg=str(e))
