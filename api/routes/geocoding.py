from fastapi import APIRouter

from api.utils.geocoding_utils import get_geocoding

router = APIRouter()


@router.get("/geocoding")
async def geocoding_route(city: str, country_code: str):
    return await get_geocoding(city, country_code)
