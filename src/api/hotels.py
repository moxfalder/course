from fastapi import APIRouter
from sqlalchemy import insert, select, func
from src.schemas.hotels import SCreate_or_PUT_hotel, SUpdate_hotel
from src.api.dependencies.pagination import pagination_params
from src.api.dependencies.get_hotel import get_hotels_params
from src.db import async_session_maker
from src.models.hotels import MHotels
from src.repositories.hotels import HotelRepo

router = APIRouter(prefix="/hotels", tags=['Отели'])


@router.get("", summary="Получение всех имеющихся отелей")
async def get_hotels(
    hotel_params: get_hotels_params,
    pagination_params: pagination_params
    ):
        # limit = pagination_params.per_page
        # offset = (pagination_params.page - 1) * pagination_params.per_page
        async with async_session_maker() as session:
            return await HotelRepo(session).get_all(
                hotel_name = hotel_params.hotel_name,
                hotel_location = hotel_params.hotel_location,
                limit = pagination_params.per_page,
                offset = (pagination_params.page - 1) * pagination_params.per_page
            )        


@router.post("", summary="Добавление отеля")
async def create_hotel(hotel_data: SCreate_or_PUT_hotel):

    async with async_session_maker() as session:
        hotel = await HotelRepo(session).add(**hotel_data.model_dump())
        print(type(str(hotel)))
        
        await session.commit()

    return {"status": "OK", "data": str(hotel)}


@router.put("/hotels/{hotel_id}", summary="Изменение отеля")
def update_all_params_hotel(
        hotel_id: int,
        hotel_data: SCreate_or_PUT_hotel
):

    for hotel in hotels:
        if hotel["hotel_id"] == hotel_id:
            if len(hotel_data.hotel_name) != 0:
                hotel['hotel_name'] = hotel_data.hotel_name
            if len(hotel_data.hotel_location) != 0:
                hotel['hotel_location'] = hotel_data.hotel_location

            # hotel = {"hotel_id": hotel_id,
            #          "hotel_name": updated_hotel_name,
            #          "hotel_location": updated_hotel_location
            #          }
            return {"status": "OK"}
    # for hotel in hotels:
    #     if hotel["hotel_id"] == hotel_id:
    #         updated_hotel_name = hotel["hotel_name"] = hotel_name
    #         updated_hotel_location = hotel["hotel_location"] = hotel_location
    #         hotel = {"hotel_id": hotel_id,
    #                          "hotel_name": updated_hotel_name,
    #                          "hotel_location": updated_hotel_location
    #                          }
    #         return hotel
        # return {"status": "OK"}


@router.patch("/{hotel_id}", summary="Изменение значений полей отеля")
def update_one_or_more_params_hotel(
        hotel_id: int,
        hotel_data: SUpdate_hotel
):
    for hotel in hotels:
        if hotel["hotel_id"] == hotel_id:
            if hotel_data.hotel_name:
                hotel["hotel_name"] = hotel_data.hotel_name
            if hotel_data.hotel_location:
                hotel["hotel_location"] = hotel_data.hotel_location
    return {"status": "OK"}


@router.get("/{id}", summary="Получение отеля по его идентификатору")
def get_hotel(hotel_id: int):
    for hotel in hotels:
        if hotel["hotel_id"] == hotel_id:
            return hotel
        # return {"status": "OK"}


@router.delete("/{hotel_id}", summary="Удаление отеля")
def delete_hotel(hotel_id: int):
    global hotels
    for hotel in hotels:
        if hotel['hotel_id'] == hotel_id:
            hotels.remove(hotel)
    return {"status": 'OK'}