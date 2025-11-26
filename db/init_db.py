from sqlmodel import SQLModel,create_engine

db_path = "sqlite:///C:/Users/meyers/Desktop/IDF_SEST/db/Seven_Harvests_Residential_Placement.db"
engine = create_engine(db_path,echo=True)

def create_db_and_tables()-> None:
    SQLModel.metadata.create_all(engine)

