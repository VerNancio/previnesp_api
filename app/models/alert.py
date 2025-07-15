from pydantic import BaseModel

class Alert(BaseModel):
    nome: str
    preco: float
