from fastapi import APIRouter,Depends, FastAPI,Body, Path, Query
from fastapi.responses import HTMLResponse,JSONResponse
from fastapi.encoders import jsonable_encoder
#import paquete donde creo todos los modelos para el uso del api
from models.Movie import Movie
from models.Entities.movie import Movie as MovieModel
from typing import  List

#uso paquetes para conexion a sql
from config.database import Base, Session, engine

movie_router = APIRouter()


@movie_router.get('/movies',tags=['movies'],response_model=List[Movie],status_code=200)
def Movies() -> List[Movie]:
    db = Session()
    result= db.query(MovieModel).all()
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

    


@movie_router.get('/movies/{id}',tags=['movies'],response_model=Movie,status_code=200)
def get_movie(id:int=Path(ge=1,le=2000)):
    db= Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404,content={'message':'No encontrado'})
    return JSONResponse(status_code=200,content=jsonable_encoder(result))


@movie_router.get('/movies/',tags=['movies'])
def get_movies_by_category(category:str=Query(min_length=2, max_length=100),year:int=Path(ge=1800,le=2030)):
    db= Session()
    result= db.query(MovieModel).filter(MovieModel.category == category).all()
    return JSONResponse(status_code=200,content=jsonable_encoder(result))


@movie_router.post('/movies',tags=['movies'])
def create_movie(movie:Movie):
    db= Session()
    new_movie=MovieModel(**movie.model_dump())
    db.add(new_movie)
    db.commit()
    

    return JSONResponse(content={"message":"Se ha agregado la pelicula"})

@movie_router.put('/movies',tags=['movies'])
def update_movie(id:int,mov:Movie):
    db= Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404,content={'message':'No encontrado'})
    
    result.title= mov.title
    result.overview=mov.overview
    result.year= mov.year
    result.rating=mov.rating
    result.category=mov.category
    db.commit()
    return JSONResponse(content={"message":"Se ha actualizado la pelicula"})

    

@movie_router.delete('/movies',tags=['movies'])
def delete_movie(id:int):
    db= Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404,content={'message':'No encontrado'})
    
    db.delete(result)
    db.commit()
    return JSONResponse(content={"message":"Se ha eliminado la pelicula"})
