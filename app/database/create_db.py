from app.database.connection import engine, Base
from app.models.game import Game

Base.metadata.create_all(bind=engine)