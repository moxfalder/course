from sqlalchemy import select,insert
from pydantic import BaseModel


class BaseRepo:
    model = None

    def __init__(self, session):
        self.session = session
    
    async def get_all(self, *args, **kwargs):
    
        query = select(self.model)
        result = await self.session.execute(query)
        return result.scalars().all()
    
    async def add(self, data: BaseModel):
        data_stmt = insert(self.model).values(**data.model_dump()).returning(self.model)
        
        # res = stmt.compile(compile_kwargs={"literal_binds": True})
        res = await self.session.execute(data_stmt)
        return res.scalars().one()
    

    async def edit(self):
        ...


    async def delete(self):
        ...

         
