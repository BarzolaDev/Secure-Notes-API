from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.core.security import decode_token
from app.db.mongo import users_collection

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)

    if payload is None:
        raise HTTPException(status_code=401, detail='Invalid token')
    
    email = payload.get("sub")

    user = users_collection.find_one({"email": email})

    if user is None:
        raise HTTPException(status_code=404, detail = "User not found")
    
    user["_id"] = str(user["_id"])
    user.pop("password")
    
    return user




