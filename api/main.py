from fastapi import FastAPI

from api.routes.geocoding import router as geocoding_router

app = FastAPI()

app.include_router(geocoding_router)
