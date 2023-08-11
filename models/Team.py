from pydantic import BaseModel,Field
from typing import Optional

class Team(BaseModel):
     id:Optional[int] = None
     Name:str
     YearFoundation:int
     Nacionality:int
     Country:int