from models.Entities.movie import Movie as MovieModel
from models.Movie import Movie as mv
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
    
    def create_movie(self,movie:mv):
        result= MovieModel(**movie.model_dump())
        self.db.add(result)
        self.db.commit()
        return 
    
    def update_movie(self,id:int,data:mv):
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        movie.title= data.title
        movie.overview= data.overview
        movie.year = data.year
        movie.rating= data.rating
        movie.category= data.category
        self.db.commit()
        return
    
    def delete_movie(self,id:int):
        self.db.query(MovieModel).filter(MovieModel.id==id).delete()
        self.db.commit()
        return