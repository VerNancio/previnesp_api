from fastapi import FastAPI
from app.api import routes_produtos, routes_usuarios

app = FastAPI()

app.include_router(routes_produtos.router, prefix="/produtos")
app.include_router(routes_usuarios.router, prefix="/usuarios")
