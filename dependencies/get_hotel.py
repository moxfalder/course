from typing import Annotated
from fastapi import Query, Depends
from pydantic import BaseModel

class SHotels(BaseModel):
    hotel_id: Annotated[int | None, Query(None, description="ID отеля")]
    hotel_name: Annotated[str | None, Query(None, description="Название отелей")]


get_hotels_params = Annotated[SHotels, Depends()]