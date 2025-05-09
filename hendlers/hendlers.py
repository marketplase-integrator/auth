from model.models import User
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.post("/register")
async def register_user(user:User):
    try:
        return {"massage": "Пользователь сохранен", "user": user.model_dump()}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
