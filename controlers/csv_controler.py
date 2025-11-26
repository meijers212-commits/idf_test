import csv
import io
from fastapi import UploadFile, File, HTTPException
from sqlalchemy import MetaData
from sqlmodel import Session

from db.init_db import engine
from sqlalchemy import MetaData, Table, Column, String


def convert_csv_to_matrix(file: UploadFile):

    if file.content_type != "text/csv":
        raise HTTPException(status_code=400, detail="need to be 'CSV' file only.")

    content = file.file.read()

    try:
        decoded = content.decode("utf-8")
    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="file cant be decode by - UTF-8")

    reader = csv.reader(io.StringIO(decoded))
    rows = [row for row in reader]

    return rows



def create_table_from_csv(table_name: str, rows: list[list[str]]):
    headers = rows[0]
    data = rows[1:]

    metadata = MetaData()
    metadata.reflect(bind=engine)

    if table_name in metadata.tables:
        metadata.tables[table_name].drop(engine)

    columns = [Column(h, String) for h in headers]

    new_table = Table(table_name, metadata, *columns)
    metadata.create_all(engine)

    with engine.connect() as conn:
        for row in data:
            data_dict = {headers[i]: row[i] for i in range(len(headers))}
            conn.execute(new_table.insert().values(**data_dict))

        conn.commit()


def insert_csv_to_existing_table(table_name,rows: list[list[str]]):
    headers = rows[0]       # כותרות CSV
    data = rows[1:]         # שורות נתונים

    with Session(engine) as session:
        for row in data:
            item_data = {headers[i]: row[i] for i in range(len(headers))}
            table = table_name(**item_data)
            session.add(table)

        session.commit()