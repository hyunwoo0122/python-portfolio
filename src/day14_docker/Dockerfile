# 1. Python 베이스 이미지
FROM python:3.11

# 2. 작업 폴더
WORKDIR /app

# 3. requirements 먼저 복사
COPY requirements.txt .

# 4. 라이브러리 설치
RUN pip install --no-cache-dir -r requirements.txt

# 5. 프로젝트 전체 복사
COPY . .

# 6. 사용할 포트
EXPOSE 8000

# 7. FastAPI 실행
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]