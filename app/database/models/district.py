# import geopy.location
from ..core import Base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship
# import geopy


class District(Base):
    __tablename__ = 'districts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    lat = Column(Float(11))
    lon = Column(Float(11))

    previsions = relationship('Prevision', back_populates='district')
    alerts = relationship('Alert', back_populates='district')



    def __init__(self, name: str, lat: float, lon: float):

        if len(name) > 20: raise ValueError('Erro: String do parametro "name" tem mais de 20 caractéres')

        self.name = name
        self.lat = lat
        self.lon = lon
    

