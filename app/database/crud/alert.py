from sqlalchemy import Session

from ..models.alert import Alert
from ..models.district import District

import datetime as dt

from typing import Optional, List


def create_alert(db: Session, start_date: dt.date, start_horary: dt.time, 
                 end_date: dt.date, end_horary: dt.time, 
                 alertLevel: int, message: str, type: str,
                 district: District) -> Alert:

    new_Alert = Alert(start_date,start_horary,end_date,end_horary,alertLevel,message,type,district)

    db.add(new_Alert)
    db.commit()
    db.refresh()
    return new_Alert

def get_alert(db: Session, id: int) -> Optional[Alert]:
    return db.query(Alert).filter(Alert.id == id).first()

def get_alerts(db: Session) -> List[Alert]:
    return db.query(Alert).all()

def up_start_date_alert(db: Session, start_date: dt.date, start_horary: dt.time, 
                      end_date: dt.date, end_horary: dt.time, 
                      alertLevel: int, message: str, type: str,
                      district: District) -> Optional[Alert]:
    
    alert = db.query(Alert).filter(Alert.id == id).first()

    if not alert:
        return None
    
    alert.start_date = start_date
    alert.start_horary = start_horary
    alert.end_date = end_date
    alert.end_horary = end_horary
    alert.alertLevel = alertLevel
    alert.messade = message
    alert.type = type
    alert.district = district
    
    db.commit()
    db.refresh()
    return alert

def delete_alert(db: Session) -> bool:

    alert = db.query(Alert).filter(Alert.id == id).first()
    
    if not alert:
        return False
    
    db.delete(alert)
    db.commit()
    return True