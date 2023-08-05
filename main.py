from typing import List
from fastapi import FastAPI,Body, Path, Query
from fastapi.responses import HTMLResponse,JSONResponse
#importo paquete donde tengo la data de un diccionario de peliculas
import data.infoMovies as im
#import paquete donde creo todos los modelos para el uso del api
import models.Movie as Mv
import models.identity.User as us
import Security.identity as id 


from Security.Token.jwt_manager import create_token

app= FastAPI()


app.title=" Mi aplicacion con fastapi"
app.version="1.0.0"


@app.post('/Login',tags=['Login'])
def login(user:us.User)-> str:
    if id.valid_user(user):
        return JSONResponse(id.get_token(user),status_code=200)
    else:
        return JSONResponse("Credenciales erroneas",status_code=401)
    


@app.get('/',tags=['Home'])
def message():
    return HTMLResponse('<h1>Hola Mundo </h1>')


@app.get('/movies',tags=['movies'],response_model=List[Mv.Movie],status_code=200)
def Movies():
    return JSONResponse(status_code=200,content=im.movies)


@app.get('/movies/{id}',tags=['movies'])
def get_movie(id:int=Path(ge=1,le=2000)):
    return JSONResponse(content=[item for item in im.movies if item["id"]==id])


@app.get('/movies/',tags=['movies'])
def get_movies_by_category(category:str=Query(min_length=2, max_length=100),year:int=Path(ge=1800,le=2030)):
    data=[item for item in im.movies if item["title"]==category or int(item["year"])==year]
    return JSONResponse(content=data)

@app.post('/movies',tags=['movies'])
def create_movie(movie:Mv.Movie):
    im.movies.append(
        movie
    )

    return JSONResponse(content={"message":"Se ha agregado la pelicula"})

@app.put('/movies',tags=['movies'])
def update_movie(id:int,mov:Mv.Movie):
    listaNueva= [{**movie,"title":mov.title,"overview":mov.overview,"year":mov.year,"rating":mov.rating,"category":mov.category} if int(movie["id"])==id else movie for movie in im.movies]
    im.movies.clear()
    im.movies=listaNueva
    return JSONResponse(content={"message":"Se ha modificado la pelicula"})

@app.delete('/movies',tags=['movies'])
def delete_movie(id:int):
    [(movie,im.movies.remove(movie)) for movie in im.movies if int(movie["id"])==id]
    return JSONResponse(content={"message":"Se ha eliminado la pelicula"})