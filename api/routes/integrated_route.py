from fastapi import APIRouter, HTTPException

from api.utils.forecast_utils import get_forecast
from api.utils.geocoding_utils import get_geocoding

router = APIRouter()


@router.get("/geocoding_and_forecast")
async def geocoding_and_forecast_route(city: str, country_code: str):
    geocodes = await get_geocoding(city, country_code)
    if not geocodes:
        raise HTTPException(
            status_code=404,
            detail=f"No data for city: {city}, country_code: {country_code}",
        )
    latitude, longitude = geocodes[0]["lat"], geocodes[0]["lon"]
    return await get_forecast(latitude, longitude)
