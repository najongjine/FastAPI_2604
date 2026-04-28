from typing import Generic, TypeVar, Any, Optional
from pydantic import BaseModel

T = TypeVar("T")

class CommonResponse(BaseModel, Generic[T]):
    success: bool=True
    data: Optional[T] = None
    msg: str = ""
