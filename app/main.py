from fastapi import FastAPI
from app.routes import routes_alerts, routes_previsions
from app.database.init_db import init_db

app = FastAPI()

@app.on_event("startup")
def startup_event():
    init_db()

app.include_router(routes_alerts.router, prefix="/alerts")
app.include_router(routes_previsions.router, prefix="/previsions")
