from typing import Annotated
from pydantic import BaseModel
from fastapi import Depends,Query

class Pagination_params(BaseModel):
    per_page: Annotated[int | None, Query(5, ge=1, le=50, description="Количество выводимых элементов на странице"),]
    page: Annotated[int  | None, Query(1, ge=1, description="Номер страницы")]

pagination_params = Annotated[Pagination_params, Depends()]