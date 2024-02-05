from fastapi import APIRouter

from api.utils.geocoding_utils import get_geocoding

router = APIRouter()


@router.get("/geocoding")
async def geocoding_route(country: str, code: str):
    return await get_geocoding(country, code)
