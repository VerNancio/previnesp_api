from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..models.prevision import Prevision

router = APIRouter()

@router.get('/day/{day}')
def get_day_weather(day: int, db: Session = Depends(get_db)):
    return


@router.get('/days')
def get_days_weather(firtDay: int, lastDay: int, db: Session = Depends(get_db)):
    return


@router.get('/days/more_infos')
def get_days_weather(firtDay: int, lastDay: int, startHorary: int, endHorary: int, zone: str, db: Session = Depends(get_db)):
    return