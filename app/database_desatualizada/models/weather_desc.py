from database.core import Base
from sqlalchemy import Column, String, Integer, Float


class Weather_desc(Base):
    __tablename__ = 'weather_descs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    desc = Column(String(40))


    def __init__(self, desc: str):

        if len(desc) > 40: raise ValueError(f'Erro: conteúdo da str possuí mais de 40 caractéres')
        
        self.desc = desc
    

