from fastapi import FastAPI
from app.routes import room, guess  # you'll make these soon

app = FastAPI()

# Register routes
app.include_router(room.router, prefix="/room", tags=["Room"])
app.include_router(guess.router, prefix="/guess", tags=["Guess"])

@app.get("/")
def read_root():
    return {"message": "Word Battle API is up"}