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
    id: Optional[int] = Field(default=None, primary_key=True, foreign_key = "web_user.id", ondelete="CASCADE")
    
class Attendee(SQLModel, table = True):
    __tablename__ = "attendee"
    id: Optional[int] = Field(default = None, primary_key = True, foreign_key = "web_user.id", ondelete="CASCADE")

class Calendar(SQLModel, table = True):
    __tablename__ = "calendar"
    id: Optional[int] = Field(default = None, primary_key  = True)
    name: str = Field(max_length = 50, nullable = False)
    period: datetime = Field(default = None)

class Create_Schedule(SQLModel, table = True):
    __tablename__ = "create_schedule"
    hostID: int = Field(primary_key = True, foreign_key = "host.id", ondelete="CASCADE")
    calendarID: int = Field(primary_key = True, foreign_key = "calendar.id", ondelete="CASCADE")
    time_create: datetime = Field(default_factory = datetime.now)

class Vote(SQLModel, table = True):
    __tablename__ = "vote"
    attendeeID: int = Field(primary_key = True, foreign_key = "attendee.id", ondelete="CASCADE")
    calendarID: int = Field(primary_key = True, foreign_key = "calendar.id", ondelete="CASCADE")