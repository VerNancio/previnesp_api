import geopy.location
from database.core import Base
from sqlalchemy import Column, String, Integer, Float
import geopy


class District(Base):
    __tablename__ = 'districts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    lat = Column(Float(11))
    lon = Column(Float(11))


    def __init__(self, name: str, lat: float, lon: float):

        if len(name) > 20: raise ValueError('Erro: String do parametro "name" tem mais de 20 caractéres')

        self.name = name
        self.lat = lat
        self.lon = lon
    

