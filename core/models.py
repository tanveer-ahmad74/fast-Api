from core.database import Base
from datetime import datetime, timezone
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy import Boolean
from sqlalchemy import DateTime


def dt_utc_now():
    return datetime.now(timezone.utc)


class SoftDeletion(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    is_deleted = Column(Boolean, default=False)


class Colour(SoftDeletion):
    __tablename__ = 'Colour'

    name = Column(String)
    hex_code = Column(String)
