from pydantic import BaseModel

class GameCreate(BaseModel):
    name: str
    description: str
    price: int
    gender: str
    progress: str

class GameRead(GameCreate):
    id: int

    class Config:
        orm_mode = True
