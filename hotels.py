from fastapi import APIRouter, Query, Body
from schemas.hotels import SCreate_or_PUT_hotel, SUpdate_hotel

router = APIRouter(prefix="/hotels", tags=['Отели'])



hotels = [
    {"hotel_id": 1,
     "hotel_name": "Neman",
     "hotel_location": 'РБ'
     },
    {"hotel_id": 2,
     "hotel_name": "Belarus",
     "hotel_location": 'РБ'
     },
    {"hotel_id": 3,
     "hotel_name": "Turist",
     "hotel_location": 'РБ'
     },
    {"hotel_id": 4,
     "hotel_name": "Kronon",
     "hotel_location": 'РБ'
     },
    {"hotel_id": 5,
     'hotel_name': 'Semashko',
     "hotel_location": 'РБ'
     }
     ,
    {"hotel_id": 6,
     'hotel_name': 'EcoHouse',
     "hotel_location": 'РБ'
     },
    {"hotel_id": 7,
     'hotel_name': 'VSDesign',
     "hotel_location": 'РБ'
     },
    {"hotel_id": 8,
     'hotel_name': 'Slavia',
     "hotel_location": 'РБ'
     }
]

@router.get("", summary="Получение всех имеющихся отелей")
def get_hotels(
    hotel_id: int | None = Query(None, description="ID отеля"),
    hotel_name: str | None = Query(None, description="Название отелей"),
    per_page: int | None = Query(3, description="Количество элементов"),
    page: int  | None = Query(1, description="Номер страницы")
    ):
    hotels_list = []
    for hotel in hotels:
        if hotel_id and hotel["hotel_id"] != hotel_id:
            continue
        if hotel_name and hotel["hotel_name"] != hotel_name:
            continue
        hotels_list.append(hotel)

    if page:
        return hotels_list[(page - 1) * per_page: page * per_page]




@router.post("", summary="Добавление отеля")
def create_hotel(hotel_data: SCreate_or_PUT_hotel):
    # length = len(hotels)
    new_id = len(hotels) + 1
    new_hotel = {"hotel_id": new_id,
                 "hotel_name": hotel_data.hotel_name,
                 "hotel_location": hotel_data.hotel_location
                 }
    hotels.append(new_hotel)
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