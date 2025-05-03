from pydantic import BaseModel

class Room(BaseModel):
    room_code: str
    player1: str | None
    player2: str | None
    state: str  # "waiting", "playing", "finished"
    turn: str | None