from pydantic import BaseModel

class WatchlistCreate(BaseModel):
    movie_id: int
    movie_title: str
    note: str

class WatchlistUpdate(BaseModel):
    movie_id: int
    note: str