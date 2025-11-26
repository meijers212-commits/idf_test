from sqlmodel import SQLModel, Field

class Rooms(SQLModel, table=True):
    id: int = Field(primary_key=True)
    apartment_id: int
    room_id: int
    soldier_id: int




