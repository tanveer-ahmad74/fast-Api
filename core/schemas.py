from pydantic import BaseModel
from pydantic import validator

from core.database import get_db
from core.models import Colour
from datetime import datetime

db = next(get_db())


class ColorCreateUpdate(BaseModel):
    name: str
    hex_code: str
    is_deleted: bool

    class Config:
        orm_mode = True
        db_model = Colour


class ColorList(BaseModel):
    id: int
    name: str
    hex_code: str
    is_deleted: bool

    class Config:
        orm_mode = True