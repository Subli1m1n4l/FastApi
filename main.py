from fastapi import Depends, FastAPI
from fastapi.responses import HTMLResponse,JSONResponse

#importo paquete donde tengo la data de un diccionario de peliculas
from Security.JWTBearer import JWTBearer

import models.identity.User as us
import Security.identity as id 
#uso paquete de openIA
import openai

#uso paquetes para conexion a sql
from config.database import Base, engine


#uso paquete para mapper de entidades
from automapper import mapper
#uso middleware para manejo de errores
from middlewares.error_handler import ErrorHandler
#importo routers
from routers.movie import movie_router
openai.api_key = ""


from Security.Token.jwt_manager import create_token

app= FastAPI()
app.title=" Mi aplicacion con fastapi"
app.version="1.0.0"
app.add_middleware(ErrorHandler)
app.include_router(movie_router)
Base.metadata.create_all(bind=engine)


@app.post('/Login',tags=['Login'])
def login(user:us.User)-> str:
    if id.valid_user(user):
        return JSONResponse(id.get_token(user),status_code=200)
    else:
        return JSONResponse("Credenciales erroneas",status_code=401)
    


@app.get('/',dependencies=[Depends(JWTBearer())],tags=['Home'])
async def message():
    return HTMLResponse('<h1>Hola Mundo </h1>')



#seccion de trabajo pineda

@app.get('/teams',tags=['Soccer'])
def get_teams():
    return ""


@app.get('teamsCount',tags=['Soccer'])
def teamsCount():
    return ""

@app.get('teamsChampionsCount',tags=['Soccer'])
def teamChampionsCount(team:str):
    return ""

@app.get('teamsTotalChampionsCount',tags=['Soccer'])
def teamsTotalChampionsCount():
    return ""


# seccion de trabajo con openIA

@app.get('/chat',tags=['Chats'])
def get_chat(mensaje:str):
    completion = openai.ChatCompletion.create(
    model="text-davinci-002",
    messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": f"{mensaje}"}
    ]
    )


    return HTMLResponse(f"<Body><h1>Esta es la respuesta generada por chatgpt</h1> \
                        {completion.choices[0].message}</body>")