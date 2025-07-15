from ..core import Base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship


class Weather_desc(Base):
    __tablename__ = 'weather_descs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(Integer, nullable=False)
    desc = Column(String(40))

    previsions = relationship('Prevision', back_populates='weather_desc')


    def __init__(self, code: int, desc: str):

        if len(desc) > 40: 
            raise ValueError(f'Erro: conteúdo da str possuí mais de 40 caractéres')
        if code < 0:
            raise ValueError(f'Erro: código menor que zero (inválido)')
        
        self.code = code
        self.desc = desc
    

