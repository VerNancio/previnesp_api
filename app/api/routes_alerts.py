from fastapi import APIRouter
from ..models.alert import Alert

router = APIRouter()


@router.get("/")
def listar_produtos():
    return [{"id": 1, "nome": "Camiseta"}]


@router.get('/alerts')
def get_day_weather():
    return


@router.get('/alerts/{zone}')
def get_day_weather(zone: int):
    return


@router.get('/alerts/days/{number_of_days}')
def get_days_weather():
    return