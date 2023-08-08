from fastapi import APIRouter,Depends, FastAPI,Body, Path, Query
from fastapi.responses import HTMLResponse,JSONResponse
from fastapi.encoders import jsonable_encoder
#import paquete donde creo todos los modelos para el uso del api
from models.identity.User import User
#uso paquetes para conexion a sql
from config.database import Base, Session, engine
#uso paquete para validar usuario y crear token
from Security.identity import valid_user,get_token
import Security.identity as id
aut_router = APIRouter()

@aut_router.post('/Login',tags=['Login'])
def login(user:User)-> str:
    if valid_user(user):
        return JSONResponse(get_token(user),status_code=200)
    else:
        return JSONResponse("Credenciales erroneas",status_code=401)