from sqlalchemy import create_engine
from sqlalchemy.orm import session, declarative_base
import os

DB_URL = os.getenv('DB_URL', 'mysql+pymysql://root:root@localhost:3306/previnesp_bd')

engine = create_engine()
Session = session(bind=engine)
Base = declarative_base()