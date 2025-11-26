from sqlmodel import SQLModel,Field
from  typing import Optional

class Drom(SQLModel,table=True):
    prymery: int = Field(default=None,primary_key=True)
    apartment_id: int
    room_id: int
    count_solders_in_room: Optional[int] = Field(default=0)


