from sqlalchemy.orm import Session

from ..models.prevision import Prevision
from ..models.district import District
from ..models.weather_desc import Weather_desc

import datetime as dt

from typing import Optional, List


def create_prevision(db: Session, date: dt.time, horary: dt.time, 
                     temp_min: float, temp_max: float, precipitation: float, humidity: float, wind_speed: float,
                     district: District, weather_desc: Weather_desc) -> Prevision:

    new_prevision = Prevision(date,horary,temp_min,temp_max,precipitation,humidity,wind_speed,district,weather_desc)

    db.add(new_prevision)
    db.commit()
    db.refresh()
    return new_prevision

def get_prevision(db: Session, id: int) -> Optional[Prevision]:
    return db.query(Prevision).filter(Prevision.id == id).first()

def get_previsions(db: Session) -> List[Prevision]:
    return db.query(Prevision).all()

def update_prevision(db: Session,  date: dt.time, horary: dt.time, 
                     temp_min: float, temp_max: float, precipitation: float, humidity: float, wind_speed: float,
                     district: District, weather_desc: Weather_desc) -> Optional[Prevision]:
    
    prevision = db.query(Prevision).filter(Prevision.id == id).first()

    if not prevision:
        return None
    
    prevision.date = date
    prevision.horary = horary
    prevision.temp_min = temp_min
    prevision.temp_max = temp_max
    prevision.precipitation = precipitation
    prevision.humidity = humidity
    prevision.wind_speed = wind_speed
    prevision.district = district
    prevision.weather_desc = weather_desc

    db.commit()
    db.refresh()
    return prevision

def delete_prevision(db: Session) -> bool:
    prevision = db.query(Prevision).filter(Prevision.id == id).first()
    
    if not prevision:
        return False
    
    db.delete(prevision)
    db.commit()
    return True