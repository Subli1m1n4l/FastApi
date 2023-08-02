from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import data.infoMovies as im
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
