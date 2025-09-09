from sqlalchemy import select,insert


class BaseRepo:
    model = None

    def __init__(self, session):
        self.session = session
    
    async def get_all(self, *args, **kwargs):
    
        query = select(self.model)
        result = await self.session.execute(query)
        return result.scalars().all()
    
    async def add(self, **params):
        stmt = insert(self.model).values(**params)
        
        res = stmt.compile(compile_kwargs={"literal_binds": True})
        await self.session.execute(stmt)
        return res
         
