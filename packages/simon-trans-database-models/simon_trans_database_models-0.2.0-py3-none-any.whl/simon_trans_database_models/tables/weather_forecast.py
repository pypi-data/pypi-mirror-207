from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy.dialects.mysql import DOUBLE

from .base import Base


class WeatherForecast(Base):
    __tablename__ = "weather_forecast"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    date = Column(DateTime, nullable=False)
    sunshine_time = Column(
        Integer, nullable=False, comment="Sunshine time is the amount of minutes with expected sunshine."
    )
    low_clouds = Column(
        DOUBLE,
        nullable=False,
        comment="0 - 4 km/ below an altitude of 640 hPa (5 km at equator). Cloud cover is expressed in percent (%).",
    )
    mid_clouds = Column(
        DOUBLE,
        nullable=False,
        comment="4 - 8 km/ between an altitude of 640 and 350 hPa (10 km at equator). Cloud cover is expressed in percent (%).",
    )
    high_clouds = Column(
        DOUBLE,
        nullable=False,
        comment="8 - 15 km/ between an altitude of 350 and 150 hPa (18 km at equator). Cloud cover is expressed in percent (%).",
    )
    total_cloud_cover = Column(DOUBLE, nullable=False, comment="Cloud cover is expressed in percent (%).")
    visibility = Column(
        Integer,
        nullable=False,
        comment="Visibility is the distance (in metres) at which an object can be clearly seen.",
    )
    temperature = Column(DOUBLE, nullable=False, comment="Air temperature is calculated for 2 meters above the ground.")
    felt_temperature = Column(
        DOUBLE,
        nullable=False,
        comment="Felt temperature is the perceived temperature that people experience. It considers the cooling effect of wind (wind chill) as well as heating effects caused by relative humidity, radiation and low wind speeds.",
    )
    wind_speed = Column(
        DOUBLE,
        nullable=False,
        comment="Wind speed is the rate at which air is moving horizontally. meteoblue expresses wind speed in meter per second (m/s).",
    )
    wind_direction = Column(
        Integer,
        nullable=False,
        comment="It is the direction from which the wind blows (e.g. north wind comes from the north and blows to the South corresponding to a direction of 0 degrees). It is expressed in degree (°).",
    )
    relative_humidity = Column(
        DOUBLE,
        nullable=False,
        comment="Relative humidity indicates how saturated the air is with moisture (expressed in percent (%)).",
    )
    sea_level_pressure = Column(
        DOUBLE,
        nullable=False,
        comment="It is the atmospheric pressure at sea level. For locations which are not at sea level, the pressure is corrected to represent pressure at sea level. Sea level pressure is expressed in hectopascal (hPa).",
    )
    precipitation_probability = Column(
        DOUBLE,
        nullable=False,
        comment="Precipitation probability is the likelihood with which a precipitation amount of more than 0.2 mm of rain occurs within the time window of the last one, three or 24 hours, respectively.",
    )
    convective_precipitation = Column(
        DOUBLE,
        nullable=False,
        comment="Convective precipitation is caused by convective weather (e.g. thunderstorms). Therefore, air rises into the atmosphere, because of extreme heat. When air rises to high atmospheric levels, it cools down and consequently, vapour condenses into precipitation.",
    )
    is_day_light = Column(
        DOUBLE,
        nullable=False,
        comment="Daylight duration is defined as the time between sunrise and sunset. It is dependent on the latitude and the time of the year. It is given in minutes per hour (min/h).",
    )
    uv_index = Column(
        Integer,
        nullable=False,
        comment="The ultraviolet index (UV index) is an international standard measurement of the strengths of the ultraviolet radiation from the sun. The purpose is to help people to effectively protect themselves from UV light. The UV index value always refers to the highest possible value that can be achieved at midday. It is expressed in index numbers from 1 to 16.",
    )
