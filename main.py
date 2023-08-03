from fastapi import FastAPI,Body
from fastapi.responses import HTMLResponse
import data.infoMovies as im
import models.Movie as Mv

app= FastAPI()


app.title=" Mi aplicacion con fastapi"
app.version="1.0.0"


@app.get('/',tags=['Home'])
def message():
    return HTMLResponse('<h1>Hola Mundo </h1>')


@app.get('/movies',tags=['movies'])
def Movies():
    return im.movies


@app.get('/movies/{id}',tags=['movies'])
def get_movie(id:int):
    return [item for item in im.movies if item["id"]==id]


@app.get('/movies/',tags=['movies'])
def get_movies_by_category(category:str,year:int):
    return [item for item in im.movies if item["title"]==category or int(item["year"])==year]


@app.post('/movies',tags=['movies'])
def create_movie(movie:Mv.Movie):
    im.movies.append(
        movie
    )

    return im.movies

@app.put('/movies',tags=['movies'])
def update_movie(id:int,mov:Mv.Movie):
    listaNueva= [{**movie,"title":mov.title,"overview":mov.overview,"year":mov.year,"rating":mov.rating,"category":mov.category} if int(movie["id"])==id else movie for movie in im.movies]
    im.movies.clear()
    im.movies=listaNueva
    return im.movies

@app.delete('/movies',tags=['movies'])
def delete_movie(id:int):
    [(movie,im.movies.remove(movie)) for movie in im.movies if int(movie["id"])==id]
    return im.movies