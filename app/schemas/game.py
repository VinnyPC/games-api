from pydantic import BaseModel


class Game(BaseModel):
    name: str
    description: str
    price: int
    gender: str
    progress: str


class GameCreate(Game):
    name: str
    description: str
    price: int
    gender: str
    progress: str


class GameRead(Game):
    id: int

    class Config:
        orm_mode = True


class GameUpdate(Game):
    name: str
    description: str
    price: int
    gender: str
    progress: str
