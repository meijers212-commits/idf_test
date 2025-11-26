from modols.apartments import Drom
from sqlmodel import Session
from db.init_db import engine


def init_dorms():
    with Session(engine) as session:
        for room_number in range(1, 11):
            room = Drom(prymery=None,apartment_id=1,room_id=room_number,count_soldiers_in_room=0)
            session.add(room)

        for room_number in range(1, 11):
            room = Drom(prymery=None,apartment_id=2,room_id=room_number,count_soldiers_in_room=0)
            session.add(room)

        session.commit()


