import httpx
from fastapi import HTTPException

from config import APPID

GEOCODING_API_URL = "http://api.openweathermap.org/geo/1.0/direct"


async def get_geocoding(country: str, code: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                GEOCODING_API_URL,
                params={"q": f"{country},{code}", "appid": str(APPID)},
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(
                status_code=e.response.status_code,
                detail=str(e),
            )
