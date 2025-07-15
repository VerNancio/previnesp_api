from ..core import Base
from sqlalchemy import Column, Integer, Date, Time, String


class Alert(Base):
    __tablename__ = 'alerts'

    
    id = Column(Integer, primary_key=True, autoincrement=True)

    # Onde o alerta vai ter como alvo, ta comentado porque nao sabemos se vamos fazer por distrito ou zona ainda
    # where_send_alert = (Interger)

    message = Column(String(50), nullable=False)

    # Data e hora de criação da linha no banco
    date_stored = Column(Date, nullable=False)
    time_stored = Column(Time, nullable=False)

