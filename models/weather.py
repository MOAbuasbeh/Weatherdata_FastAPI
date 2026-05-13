from sqlalchemy import Column,Integer,Float,DateTime,String
from db.database import Base
from datetime import datetime

class WeatherData(Base):
    __tablename__ = 'weather_data'

    id = Column(Integer,primary_key=True , index=True)

    city = Column(String, nullable=False)

    country = Column(String, nullable=False)

    temperature = Column(Float , nullable=False)

    humidity = Column(Float , nullable=False)

    weather_condition = Column(String, nullable=False)

    created_at = Column(DateTime , default=datetime.utcnow)






