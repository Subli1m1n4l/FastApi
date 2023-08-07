from typing import Any, Coroutine, Optional
from fastapi import HTTPException
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials
from starlette.requests import Request
from Security.Token import jwt_manager as jwt
from Security import identity as id
from models.identity import User as us


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth= await super().__call__(request)
        data = jwt.validate_token(auth.credentials)
        email=data['email']
        password=data['password']
        user=us.User(email=email,password=password)
        print(user)
        if not id.valid_user(user):
            raise HTTPException(status_code=403,detail="Token invalido")
        