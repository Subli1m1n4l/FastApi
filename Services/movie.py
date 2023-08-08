from models.Entities.movie import Movie as MovieModel
#uso paquetes para conexion a sql
from config.database import Session

class MovieService():

    def __init__(self,db:Session) -> None:
        self.db:Session=db

    
    def get_movies(self):
        result=self.db.query(MovieModel).all()
        return result

    def get_movie(self, id:int):
        result=self.db.query(MovieModel).filter(MovieModel.id ==id).first()
        return result