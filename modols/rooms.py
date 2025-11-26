from sqlmodel import SQLModel, Field
from apartments import Apartments

class solders_rooms(SQLModel, table=True):
    apartment_id: int
    room_id: int
    solders_id: int = Field(primary_key=True)