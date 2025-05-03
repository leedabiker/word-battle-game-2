## stubbed for now
from fastapi import APIRouter

router = APIRouter()

@router.post("/{room_code}")
def make_guess(room_code: str):
    return {"message": f"Received guess for room {room_code}"}