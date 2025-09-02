from fastapi import FastAPI, Query, Body

app = FastAPI()

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
]

@app.get("/hotels")
def get_hotels(
        hotel_id: int | None = Query(None, description="ID отеля"),
        hotel_name: str | None = Query(None, description="Название отелей")):
    hotels_list = []
    for hotel in hotels:
        if hotel_id and hotel["hotel_id"] != hotel_id:
            continue
        if hotel_name and hotel["hotel_name"] != hotel_name:
            continue
        hotels_list.append(hotel)
    return hotels_list


@app.post("/hotels")
def create_hotel(hotel_name: str = Body(embed=True)):
    # length = len(hotels)
    new_id = len(hotels) + 1
    new_hotel = {"hotel_id": new_id,
                 "hotel_name": hotel_name,
                 }
    hotels.append(new_hotel)
    return {"status": "OK"}


@app.put("/hotels/{hotel_id}")
def update_all_params_hotel(
        hotel_id: int,
        hotel_name: str = Body(min_length=1,),
        hotel_location: str = Body(min_length=1),
):
    for hotel in hotels:
        if hotel["hotel_id"] == hotel_id:
            updated_hotel_name = hotel["hotel_name"] = hotel_name
            updated_hotel_location = hotel["hotel_location"] = hotel_location
            hotel = {"hotel_id": hotel_id,
                             "hotel_name": updated_hotel_name,
                             "hotel_location": updated_hotel_location
                             }
            return hotel
        # return {"status": "OK"}


@app.patch("/hotels/{hotel_id}")
def update_params_hotel():
    ...


@app.get("/hotels/{id}")
def get_hotel(hotel_id: int):
    for hotel in hotels:
        if hotel["hotel_id"] == hotel_id:
            return hotel
        # return {"status": "OK"}


@app.delete("/hotels/{hotel_id}")
def delete_hotel(hotel_id: int):
    global hotels
    for hotel in hotels:
        if hotel['hotel_id'] == hotel_id:
            hotels.remove(hotel)
    return {"status": 'OK'}