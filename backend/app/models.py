from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

# Bảng User
class WebUser(SQLModel, table = True):
    __tablename__ = "web_user"
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(max_length=50, nullable=False)
    password: str = Field(max_length=50, nullable=False)

class Host(SQLModel, table = True):
    __tablename__ = "host"
    id: Optional[int] = Field(default=None, primary_key=True)
    