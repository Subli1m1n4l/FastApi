from pydantic import BaseModel,Field
from typing import Optional

class Movie(BaseModel):
    id:Optional[int]= None
    title:str = Field(min_length=2,max_length=15)
    overview:str =Field(min_length=2,max_length=75)
    year:int = Field(le=2023)
    rating:float = Field(default=10, ge=1, le=10)
    category:str = Field(default='Categoría', min_length=5, max_length=15)

    