from fastapi import APIRouter
from app.firestore import db
from fastapi import HTTPException
import random
import string

router = APIRouter()

from pydantic import BaseModel

class PlayerInfo(BaseModel):
    player_name: str

class RoomState(BaseModel):
    room_code: str
    state: str
    player1: str | None
    player2: str | None
    turn: str | None

def generate_room_code(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

@router.post("/create")
async def create_room(player: PlayerInfo):
    code = generate_room_code()
    doc_ref = db.collection("rooms").document(code)
    doc_ref.set({
        "state": "waiting",
        "player1": player.player_name,
        "player2": None,
        "turn": None
    })
    return {"room_code": code, "message": f"{player.player_name} created and joine the room" }

@router.post("/join/{room_code}")
async def join_room(room_code: str, player: PlayerInfo):
    player_name = player.player_name

    # Validate player name
    if not player_name:
        return {"error": "Player name is required"}
    
    doc_ref = db.collection("rooms").document(room_code)
    doc = doc_ref.get()

    if not doc.exists:
        return {"error": "Room not found"}
    
    data = doc.to_dict()
    if data["player1"] is None:
        doc_ref.update({"player1": player_name})
    elif data["player2"] is None:
        doc_ref.update({"player2": player_name, "state": "playing", "turn": "player1"})
    else:
        return {"error": "Room is full"}

    return {"message": f"{player_name} joined room {room_code}"}

@router.get("/{room_code}", response_model=RoomState)
async def get_room(room_code: str):
    doc_ref = db.collection("rooms").document(room_code)
    doc = doc_ref.get()

   
    if not doc.exists:
        raise HTTPException(status_code=404, detail="Room not found")
    
    room_data = doc.to_dict()
    return {
        "room_code": room_code,
        **room_data  # Merge room data into the response
    }