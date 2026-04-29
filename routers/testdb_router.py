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

@router.get("/select_test")
def select_now(id: int = 0):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                SELECT
                *
                FROM t_test
                WHERE id = %s
                """, [id])
                row = cur.fetchall()

        data = row
        return CommonResponse(success=True, data=data)
    except Exception as e:
        return CommonResponse(success=False, msg=str(e))

@router.post("/upsert_test")
def upsert_test(id: int = Form(0), name: str = Form("")):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                if id <= 0:
                    cur.execute("""
                    INSERT INTO t_test (name)
                    VALUES (%s)
                    RETURNING id, name
                    """, [name])
                else:
                    cur.execute("""
                    UPDATE t_test
                    SET name = %s
                    WHERE id = %s
                    RETURNING id, name
                    """, [name, id])

                row = cur.fetchone()
                if not row:
                    conn.rollback()
                    return CommonResponse(success=False, msg="data not found")

                conn.commit()

        data = {
            "id": row[0],
            "name": row[1]
        }
        return CommonResponse(success=True, data=data)
    except Exception as e:
        return CommonResponse(success=False, msg=str(e))

@router.post("/delete_test")
def delete_test(id: int = Form(0)):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                DELETE FROM t_test
                WHERE id = %s
                """, [id])

                conn.commit()

        data = {
            "msg" : "delete success"
        }
        return CommonResponse(success=True, data=data)
    except Exception as e:
        return CommonResponse(success=False, msg=str(e))
