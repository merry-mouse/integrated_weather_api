from fastapi import FastAPI

from api.routes.forecast_route import router as forecast_router
from api.routes.geocoding import router as geocoding_router
from api.routes.integrated_route import router as integrated_router

app = FastAPI()

app.include_router(geocoding_router)
app.include_router(forecast_router)
app.include_router(integrated_router)
