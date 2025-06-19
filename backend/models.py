from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str

class Note(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    title: str
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
