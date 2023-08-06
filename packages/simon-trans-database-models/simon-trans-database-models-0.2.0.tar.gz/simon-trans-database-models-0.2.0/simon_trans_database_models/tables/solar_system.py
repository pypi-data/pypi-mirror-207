from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy.dialects.mysql import DOUBLE

from .base import Base


class SolarSystem(Base):
    __tablename__ = 'solar_system'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    date = Column(DateTime, nullable=False)
    current_power = Column(DOUBLE, nullable=False)
