from sqlmodel import SQLModel,Field
from  typing import Optional

class Apartments(SQLModel,table=True):
    apartment_id: int
    room_id: int = Field(primary_key=True)
    count_solders_in_room: Optional[int] = Field(default=None)
