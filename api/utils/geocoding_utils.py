import httpx
from fastapi import HTTPException

from config import APPID

GEOCODING_API_URL = "http://api.openweathermap.org/geo/1.0/direct"


async def get_geocoding(city: str, country_code: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                GEOCODING_API_URL,
                params={"q": f"{city},{country_code}", "appid": str(APPID)},
            )
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise HTTPException(
                status_code=e.response.status_code,
                detail=str(e),
            )
        # for handling connection timeouts or DNS failures
        except httpx.RequestError:
            raise HTTPException(
                status_code=503, detail="Temprarily unavailable, try later"
            )
        return response.json()
