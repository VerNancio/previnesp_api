from pydantic import BaseModel
import datetime as dt

class Prevision(BaseModel):
    date: dt.date 
    horary: dt.time 
    temp_min: float 
    temp_max: float 
    precipitation: float 
    humidity: float 
    wind_speed: float
    # district: District 
    # weather_desc: Weather_desc