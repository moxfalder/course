from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from src.db import Base


class MRoom(Base):

    __tablename__ = 'rooms'

    room_id: Mapped[int] = mapped_column(primary_key=True)
    room_title: Mapped[str]
    room_description: Mapped[str | None]
    room_price: Mapped[int]
    room_quantity: Mapped[int]
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels.hotel_id"))