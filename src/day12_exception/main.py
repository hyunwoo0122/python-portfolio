import time
import logging

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.exceptions import RequestValidationError

app = FastAPI()

# -------------------------------
# Middleware
# -------------------------------
class ProcessTimeMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        # 시작 시간
        start_time = time.time()

        # 실제 엔드포인트 실행
        response = await call_next(request)

        # 종료 시간
        end_time = time.time()

        # 처리 시간 계산
        process_time = end_time - start_time

        logging.info(
            f"{request.method} "
            f"{request.url.path} "
            f"{response.status_code} "
            f"{process_time:.3f}s"
        )

        return response


# 미들웨어 등록
app.add_middleware(ProcessTimeMiddleware)


# -------------------------------
# 테스트용 데이터
# -------------------------------
users = {
    1: "Kim",
    2: "Lee",
}


# -------------------------------
# Exception Handler
# -------------------------------
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):

    if exc.status_code == 404:
        code = "NOT_FOUND"
    elif exc.status_code == 401:
        code = "UNAUTHORIZED"
    else:
        code = "UNKNOWN_ERROR"

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": code,
                "message": exc.detail
            }
        }
    )

# -------------------------------
# Exception Handler(422)
# -------------------------------
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
):
    return JSONResponse(
        status_code=422,
        content={
            "error": {
                "code": "VALIDATION_ERROR",
                "message": "Validation failed",
                "details": exc.errors(),
            }
        },
    )

# -------------------------------
# Endpoint
# -------------------------------
@app.get("/users/{user_id}")
def get_user(user_id: int):

    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "id": user_id,
        "name": users[user_id]
    }