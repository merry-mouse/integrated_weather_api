from fastapi import APIRouter, Query

from api.utils.forecast_utils import get_forecast

router = APIRouter()


@router.get("/forecast")
async def forecast_router(
    lattitude: float = Query(..., description="latitude"),
    longitude: float = Query(..., description="longitude"),
    units: str = Query("metric", description="units of measure standard/metric"),
    mode: str = Query("json", description="response format json/xml"),
    lang: str = Query("en", description="language, en by default"),
    cnt: int = Query(10, description="number of timestamps, 10 by default"),
):
    return await get_forecast(
        lattitude,
        longitude,
        units,
        mode,
        lang,
        cnt,
    )
