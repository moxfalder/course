from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from src.db import Base


class MHotels(Base):
    __tablename__ = "hotels"

    hotel_id: Mapped[int] = mapped_column(primary_key=True)
    hotel_name: Mapped[str] = mapped_column(String(100))
    hotel_location: Mapped[str]
