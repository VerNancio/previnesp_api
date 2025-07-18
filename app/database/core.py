from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base

DB_URL = 'mysql+pymysql://root:1110@localhost:3306/previnesp_bd'
engine = create_engine(DB_URL)

Base = declarative_base()

from app.database.models import prevision
from app.database.models import weather_desc
from app.database.models import alert
from app.database.models import district
from app.database.models import prevision


print(Base.metadata.tables.keys())


# Cria todas as tabelas definidas nos models importados
Base.metadata.create_all(bind=engine)

# Session para operar no banco
session = Session(bind=engine)


def get_db():
    db = session
    try:
        yield db
    finally:
        db.close()