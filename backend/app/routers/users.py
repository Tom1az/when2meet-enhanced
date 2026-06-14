from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from app.database import get_db
from app.models import WebUser

# Khởi tạo router riêng với đuôi /users
router = APIRouter(prefix="/users", tags=["Users"])

# API đăng ký người dùng mới
@router.post("/", response_model=WebUser, status_code=status.HTTP_201_CREATED)
def create_user(user_data: WebUser, db: Session = Depends(get_db)):

    # Tìm trùng username với database
    statement = select(WebUser).where(WebUser.username == user_data.username)
    
    # Nếu có thì trả về hàng đầu tiên, nếu không trả về null
    existing_user = db.exec(statement=statement).first()

    if existing_user:
        # Nếu khác mật khẩu thì báo lỗi
        statement_password = select(WebUser).where(WebUser.username == user_data.username, WebUser.password == user_data.password)
        find_password = db.exec(statement=statement_password).first()
        if find_password:
            return user_data
        else:
            print("--------")
            print("Find Password =", find_password)
            print("User data password =", user_data.password)
            print("--------")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Sai mật khẩu")
    
    # Nếu chưa tồn tại trong db
    db.add(user_data)
    db.commit() # Đẩy dữ liệu từ hàng chờ xuống database (Hoạt động giống git)
    db.refresh(user_data) # Refersh để tự động sinh id

    return user_data # Trả về thông tin để frontend dễ nhận diện