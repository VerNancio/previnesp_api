from ..core import Base
from sqlalchemy import Column, Integer, Date, Time, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
import datetime as dt


class Alert(Base):
    __tablename__ = 'alerts'

    # from ..models.district import District

    
    id = Column(Integer, primary_key=True, autoincrement=True)

    start_date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_date = Column(Date, nullable=False)
    end_time = Column(Time, nullable=False)


    alert_level = Column(Enum('1', '2', '3', '4'), nullable=False)

    message = Column(String(100), nullable=False)

    type = Column(Enum('DIARIO', 'SEMANAL'), nullable=False)

    # chave estrangeira para district.id
    district_id = Column(Integer, ForeignKey('districts.id'))

    # relacionamento ORM à entidade District
    district = relationship('District', back_populates='alerts')


    # opcional: não é necessário, mas se quiser validar ou formatar:
    def __init__(self, start_date: dt.date, start_horary: dt.time, 
                 end_date: dt.date, end_horary: dt.time, 
                 alert_level: int, message: str, type: str,
                 district):
        
        from ..models.district import District


        if not (isinstance(start_date, dt.date) and isinstance(end_date, dt.date)):
            raise ValueError("'date' deve ser um datetime.date")
        if not (isinstance(start_horary, dt.time) and isinstance(end_horary, dt.time)):
            raise ValueError("'horary' deve ser um datetime.time")
        if not (isinstance(alert_level, int) and 0 < alert_level < 5):
            raise ValueError("'alertLevl' deve ser um int de 1 à 4")
        if type not in ['DIARIO', 'SEMANAL']:
            raise ValueError("'type' deve ser uma int com valor de ou 'DIARIO' ou 'SEMANAL'")
        if len(message) > 100:
            raise ValueError("'message' deve ser menor que 50")
        if not isinstance(district, District):
            raise ValueError("'district' deve ser um District")
             
        
        self.start_date = start_date
        self.start_horary = start_horary
        self.end_date = end_date
        self.end_horary = end_horary
        self.alert_level = alert_level
        self.messade = message
        self.type = type
        self.district = district


