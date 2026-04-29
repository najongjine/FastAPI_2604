import os

import psycopg
from dotenv import load_dotenv
from fastapi import APIRouter, Form, File, UploadFile
from utils.common import CommonResponse

load_dotenv()

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
        postgres_url = os.getenv("POSTGRES_URL")
        if not postgres_url:
            return CommonResponse(success=False, msg="POSTGRES_URL is not set")

        with psycopg.connect(postgres_url) as conn:
            with conn.cursor() as cur:
                cur.execute("select now()")
                row = cur.fetchone()
        print(f"row : {row}")
        data = {
            "now": row
        }
        
        return CommonResponse(success=True, data=data)
    except Exception as e:
        return CommonResponse(success=False, msg=str(e))
