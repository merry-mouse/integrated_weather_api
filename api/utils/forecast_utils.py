import httpx
from fastapi import HTTPException

from config import APPID

FORECAST_API_URL = "https://api.openweathermap.org/data/2.5/forecast"


async def get_forecast(
    latitude: float,
    longitude: float,
    units: str = "metric",
    mode: str = "json",
    lang: str = "en",
    cnt: int = 10,
):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                FORECAST_API_URL,
                params={
                    "lat": latitude,
                    "lon": longitude,
                    "appid": APPID,
                    "units": units,
                    "mode": mode,
                    "lang": lang,
                    "cnt": cnt,
                },
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(
                status_code=e.response.status_code,
                detail=str(e),
            )
