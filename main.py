from fastapi import FastAPI
from hotels import router as hotels_router

app = FastAPI()

app.include_router(hotels_router)

