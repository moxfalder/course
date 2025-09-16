from sqlalchemy import select, func
from src.repositories.base import BaseRepo
from src.models.hotels import MHotels

class HotelRepo(BaseRepo):
    model = MHotels

    async def get_all(
            self,
            hotel_name,
            hotel_location,
            limit,
            offset
            ):
        
        query = select(MHotels)

        if hotel_name:
            query = query.filter(func.lower(MHotels.hotel_name).contains(hotel_name.strip().lower()))
        
        if hotel_location:
            query = query.filter(func.lower(MHotels.hotel_location).contains(hotel_location.strip().lower()))

        query = (
            query
            .limit(limit)
            .offset(offset)
        )

        # print(query.compile(compile_kwargs={"literal_binds": True}))
        result = await self.session.execute(query)

        return result.scalars().all()
    

    # async def add(
    #         self,
    #         **params
    # ):
        
        

