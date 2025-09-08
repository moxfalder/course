from fastapi import APIRouter
from sqlalchemy import insert, select, func
from src.schemas.hotels import SCreate_or_PUT_hotel, SUpdate_hotel
from src.api.dependencies.pagination import pagination_params
from src.api.dependencies.get_hotel import get_hotels_params
from src.db import async_session_maker
from src.models.hotels import MHotels

router = APIRouter(prefix="/hotels", tags=['Отели'])



# hotels = [
#     {"hotel_id": 1,
#      "hotel_name": "Neman",
#      "hotel_location": 'РБ'
#      },
#     {"hotel_id": 2,
#      "hotel_name": "Belarus",
#      "hotel_location": 'РБ'
#      },
#     {"hotel_id": 3,
#      "hotel_name": "Turist",
#      "hotel_location": 'РБ'
#      },
#     {"hotel_id": 4,
#      "hotel_name": "Kronon",
#      "hotel_location": 'РБ'
#      },
#     {"hotel_id": 5,
#      'hotel_name': 'Semashko',
#      "hotel_location": 'РБ'
#      }
#      ,
#     {"hotel_id": 6,
#      'hotel_name': 'EcoHouse',
#      "hotel_location": 'РБ'
#      },
#     {"hotel_id": 7,
#      'hotel_name': 'VSDesign',
#      "hotel_location": 'РБ'
#      },
#     {"hotel_id": 8,
#      'hotel_name': 'Slavia',
#      "hotel_location": 'РБ'
#      }
# ]

@router.get("", summary="Получение всех имеющихся отелей")
async def get_hotels(
    hotel_params: get_hotels_params,
    pagination_params: pagination_params
    ):
        limit = pagination_params.per_page
        offset = (pagination_params.page - 1) * pagination_params.per_page
        async with async_session_maker() as session:
            query_get_hotels = select(MHotels)
            
            # if hotel_params.hotel_id:
            #     query_get_hotels = query_get_hotels.filter_by(hotel_id = hotel_params.hotel_id)
            if hotel_params.hotel_name:
                query_get_hotels = query_get_hotels.filter(func.lower(MHotels.hotel_name).like(f"%{hotel_params.hotel_name.lower()}%"))
            # if hotel_params.hotel_location:
            #     query_get_hotels = query_get_hotels.filter(MHotels.hotel_params.hotel_location).like(f"%{hotel_params.hotel_location}%")
                

            query_get_hotels = (
                query_get_hotels
                .limit(limit)
                .offset(offset)
            )

            print(query_get_hotels.compile(compile_kwargs = {"literal_binds": True}))
            result = await session.execute(query_get_hotels)



            hotels = result.scalars().all()
            # print(type(hotels), hotels)
            return hotels

    # hotels_list = []
    # for hotel in hotels:
    #     if hotel_params.hotel_id and hotel["hotel_id"] != hotel_params.hotel_id:
    #         continue
    #     if hotel_params.hotel_name and hotel["hotel_name"] != hotel_params.hotel_name:
    #         continue
    #     hotels_list.append(hotel)

    # if pagination_params.page and pagination_params.per_page:
    #     return hotels_list[(pagination_params.page - 1) * pagination_params.per_page: pagination_params.page * pagination_params.per_page]
    # return hotels_list



@router.post("", summary="Добавление отеля")
async def create_hotel(hotel_data: SCreate_or_PUT_hotel):

    async with async_session_maker() as session:
        create_hotel_stmt = insert(MHotels).values(**hotel_data.model_dump())
        await session.execute(create_hotel_stmt)
        await session.commit()

    # length = len(hoels)
    # new_id = len(hotels) + 1
    # new_hotel = {"hotel_id": new_id,
    #              "hotel_name": hotel_data.hotel_name,
    #              "hotel_location": hotel_data.hotel_location
    #              }
    # hotels.append(new_hotel)
    return {"status": "OK"}


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