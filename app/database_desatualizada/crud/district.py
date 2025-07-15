from sqlalchemy import Session
from ..models.district import District

from typing import Optional, List


def create_district(db: Session, name: str, lat: float, lon: float) -> District:

    new_district = District(name=name, lat=lat, lon=lon)

    db.add(new_district)
    db.commit()
    db.refresh()
    return new_district

def get_district(db: Session, id: int) -> Optional[District]:
    return db.query(District).filter(District.id == id).first()

def get_districts(db: Session) -> List[District]:
    return db.query(District).all()

def update_district(db: Session, desc: str) -> Optional[District]:
    district = db.query(District).filter(District.id == id).first()

    if not district:
        return None
    
    district.desc = desc
    db.commit()
    db.refresh()
    return district

def delete_district(db: Session) -> bool:
    district = db.query(District).filter(District.id == id).first()
    
    if not district:
        return False
    
    db.delete(district)
    db.commit()
    return True