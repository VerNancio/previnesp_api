from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..models.alert import Alert
from ..database.crud.district import get_district
from ..database.core import get_db


router = APIRouter()


@router.get('/')
def get_day_weather(db: Session = Depends(get_db)):
    return get_district(db, 1)


@router.get('/{zone}')
def get_day_weather(zone: int, db: Session = Depends(get_db)):
    return


@router.get('/days/{number_of_days}')
def get_days_weather(number_of_days: int, db: Session = Depends(get_db)):
    return