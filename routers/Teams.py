from fastapi import APIRouter
from fastapi.responses import HTMLResponse,JSONResponse
from models.Team import Team
from config.dbPostgres import PSession
from models.Entities.EntitiesPG.Team import Team as tpg
team_router = APIRouter()

@team_router.post('/team',tags=['Teams'])
def set_team(team:Team):
    db = PSession()
    new_team=tpg(**team.model_dump())
    db.add(new_team)
    db.commit()
    return JSONResponse("{'message':'Equipo Insertado'}",status_code=200)
