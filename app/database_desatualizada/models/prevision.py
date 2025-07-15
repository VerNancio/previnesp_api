from sqlalchemy import Column, Integer, Numeric, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from database.core import Base
from .district import District  
from .weather_desc import Weather_desc  
import datetime as dt

class Prevision(Base):
    __tablename__ = 'previsions'

    id = Column(Integer, primary_key=True, autoincrement=True)

    # armazena só a data (YYYY-MM-DD)
    date = Column(Date, nullable=False)

    temp_min = Column(Numeric(2, 1), nullable=False)
    temp_max = Column(Numeric(2, 1), nullable=False)
    
    precipitation = Column(Numeric(3, 2), nullable=False)
    humidity = Column(Numeric(3, 2), nullable=False)
    humidity = Column(Numeric(3, 2), nullable=False)

    # armazena só o horário (HH:MM:SS)
    horary = Column(Time, nullable=False)

    # chave estrangeira para district.id
    district_id = Column(Integer, ForeignKey('district.id'), nullable=False)

    # chave estrangeira para weather_desc.id
    weather_desc_id = Column(Integer, ForeignKey('weather_desc.id'), nullable=False)
    
    # relacionamento ORM à entidade District
    district = relationship('District', back_populates='previsions')

    # relacionamento ORM à entidade Weather_desc
    weather_desc = relationship('District', back_populates='previsions')


    # opcional: não é necessário, mas se quiser validar ou formatar:
    def __init__(self, date: dt.date, horary: dt.time, 
                 temp_min: float, temp_max: float, precipitation: float, humidity: float, wind_speed: float,
                 district: District, weather_desc: Weather_desc):

        if not isinstance(date, dt.date):
            raise ValueError("`date` deve ser um datetime.date")
        if not isinstance(horary, dt.time):
            raise ValueError("`horary` deve ser um datetime.time")
        if not isinstance(district, District):
            raise ValueError("`district` deve ser um District")
        
        self.date = date
        self.horary = horary
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.precipitation = precipitation
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.district = district
        self.weather_desc = weather_desc
