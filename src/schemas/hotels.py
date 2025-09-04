from pydantic import BaseModel, Field


class SCreate_or_PUT_hotel(BaseModel):
    hotel_name: str
    hotel_location: str


class SUpdate_hotel(BaseModel):
    hotel_name: str | None = Field(None)
    hotel_location: str | None = Field(None)