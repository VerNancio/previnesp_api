# import geopy.location
from ..core import Base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship
# import geopy


class District(Base):
    __tablename__ = 'districts'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    name = Column(String(20), nullable=False)
    lat = Column(Float(11), nullable=False)
    lon = Column(Float(11), nullable=False)

    previsions = relationship('Prevision', back_populates='district')
    alerts = relationship('Alert', back_populates='district')



    def __init__(self, name: str, lat: float, lon: float):

        if len(name) > 20: raise ValueError('Erro: String do parametro "name" tem mais de 20 caractéres')

        self.name = name
        self.lat = lat
        self.lon = lon
    

