from sqlalchemy import Session
from ..models.weather_desc import Weather_desc

from typing import Optional, List


def create_weather_desc(db: Session, desc: str) -> Weather_desc:

    new_weather_desc = Weather_desc(desc=desc)
    db.add(new_weather_desc)
    db.commit()
    db.refresh(new_weather_desc)
    return new_weather_desc


def get_weather_desc(db: Session, id: int) -> Optional[Weather_desc]:
    return db.query(Weather_desc).filter(Weather_desc.id == id).first()


def get_weather_desc(db: Session) -> List[Weather_desc]:
    return db.query(Weather_desc).all()

def update_weather_desc(db: Session, desc: str) -> Optional[Weather_desc]:
    weather_desc = db.query(Weather_desc).filter(Weather_desc.id == id).first()

    if not weather_desc:
        return None
    
    weather_desc.desc = desc
    db.commit()
    db.refresh()
    return weather_desc

def delete_weather_desc(db: Session) -> bool:
    weather_desc = db.query(Weather_desc).filter(Weather_desc.id == id).first()
    
    if not weather_desc:
        return False
    
    db.delete(weather_desc)
    db.commit()
    return True