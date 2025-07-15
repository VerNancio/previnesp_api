from fastapi import APIRouter
from ..models.prevision import Prevision

router = APIRouter()

@router.get('/weather/day/{day}')
def get_day_weather(day: int):
    return


@router.get('/weather/days')
def get_days_weather(firtDay: int, lastDay: int):
    return


@router.get('/weather/days/more_infos')
def get_days_weather(firtDay: int, lastDay: int, startHorary: int, endHorary: int, zone: str):
    return