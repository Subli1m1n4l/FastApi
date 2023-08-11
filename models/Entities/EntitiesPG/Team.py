from config.dbPostgres import PBase
from sqlalchemy import Column,Integer,String,Float,INTEGER

class Team(PBase):
     __tablename__='Team'

     id= Column(Integer,primary_key=True)
     Name=Column(String)
     YearFoundation=Column(Integer)
     Nacionality=Column(Integer)
     Country=Column(Integer)
     