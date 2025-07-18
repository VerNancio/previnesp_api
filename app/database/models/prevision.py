from ..core import Base
from sqlalchemy import Column, Integer, Numeric, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
import datetime as dt

class Prevision(Base):
    __tablename__ = 'previsions'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    date = Column(Date, nullable=False)
    horary = Column(Time, nullable=False)
    temp_min = Column(Numeric(4,1), nullable=False)
    temp_max = Column(Numeric(4,1), nullable=False)
    precipitation = Column(Numeric(3, 2), nullable=False)
    humidity = Column(Numeric(3, 2), nullable=False)
    wind_speed = Column(Numeric(3, 2), nullable=True) 

    district_id = Column(Integer, ForeignKey('districts.id'), nullable=False)
    weather_desc_id = Column(Integer, ForeignKey('weather_descs.id'), nullable=False)
    
    district = relationship('District', back_populates='previsions')
    weather_desc = relationship('Weather_desc', back_populates='previsions')

    def __init__(self, date: dt.date, horary: dt.time, 
                 temp_min: float, temp_max: float, precipitation: float, humidity: float, wind_speed: float,
                 district, weather_desc):
        
        from .district import District 

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


