from pydantic import BaseModel
from typing import Optional


class TodoCreate(BaseModel):
    title: str
    priority: str = "medium"
    due: Optional[str] = None


class TodoResponse(BaseModel):
    id: int
    title: str
    status: str
    priority: str
    due: Optional[str]
    created_at: str

    class Config:
        from_attributes = True
