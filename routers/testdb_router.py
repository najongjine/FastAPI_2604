from fastapi import APIRouter, Form, File, UploadFile
from utils.common import CommonResponse
from utils.db import get_connection

router = APIRouter(
    prefix="/testdb",
    tags=["testdb"]
)

@router.get("/")
def test_home():
    try:
        return CommonResponse(success=True)
    except Exception as e:
        return CommonResponse(success=False, msg=str(e))

@router.get("/now")
def select_now():
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("select now()")
                row = cur.fetchone()

        data = {
            "now": row[0].isoformat() if row else None
        }
        return CommonResponse(success=True, data=data)
    except Exception as e:
        return CommonResponse(success=False, msg=str(e))
