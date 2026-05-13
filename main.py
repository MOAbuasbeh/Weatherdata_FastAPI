from fastapi import FastAPI, Depends
from db.database import Base , engine , SessionLocal
from models.weather import WeatherData
from service.weather_service import  fetch_data
from db.deps import get_db
from sqlalchemy.orm import  Session
from sqlalchemy import  func

Base.metadata.create_all(bind=engine)
app = FastAPI(
    title= "Weatherdata API"
)
@app.get("/")
def root():
   return {"message": "Hello FastAPI"}

@app.get("/weather/{city}")
def get_weather(city:str , db:Session = Depends(get_db)):
    weather = fetch_data(city)
    db.add(WeatherData(**weather))
    db.commit()
    return weather

@app.get("/historical_weather")
def get_data(db:Session = Depends(get_db)):
    history = db.query(WeatherData).all()
    return history

@app.get("/historical_weather/{city}")
def get_data(city : str,db:Session = Depends(get_db)):
    history = db.query(WeatherData).filter(func.lower(WeatherData.city) == city.lower())
    return history



