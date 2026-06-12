from fastapi import FastAPI, Depends
from sqlmodel import Session
from app.database import get_db

# Khởi tạo backend
app = FastAPI(title="when2meet_enhance")


@app.get("/")
def read_root():
    return {"message:" "Chào mừng đến với when2meet_enhance"}

@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    return {"status:" "Kết nối PostgreSQL bằng SQLModel thành công!"}