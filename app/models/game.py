from sqlalchemy import Column, Integer, String
from app.database.connection import Base


class Game(Base):
    __tablename__ = "game"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255))
    price = Column(Integer)
    gender = Column(String(255))
    progress = Column(String(255))
