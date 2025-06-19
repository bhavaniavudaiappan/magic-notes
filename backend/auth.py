from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from jose import jwt, JWTError, ExpiredSignatureError
from datetime import datetime, timedelta
import os
from pathlib import Path
from dotenv import load_dotenv
from utils.email_utils import send_magic_link

load_dotenv(dotenv_path=Path(__file__).resolve().parents[1] / ".env")

JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
JWT_EXP_DELTA_SECONDS = 900

router = APIRouter()

@router.post("/auth/send")
def send_link(email: str):
    token = jwt.encode({"sub": email, "exp": datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)}, JWT_SECRET, algorithm=JWT_ALGORITHM)
    try:
        send_magic_link(email, token)
        return {"message": "Magic link sent"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class TokenData(BaseModel):
    token: str

@router.post("/auth/verify")
def verify_token(data: TokenData):
    try:
        payload = jwt.decode(data.token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return {"email": payload["sub"]}
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")