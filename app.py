from fastapi import FastAPI
from routers import test_router, testdb_router
import uvicorn

app = FastAPI()

app.include_router(test_router.router)
app.include_router(testdb_router.router)


@app.get("/")
def home():
    return {"message": "FastAPI 실행 성공"}


if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
