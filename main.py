import uvicorn
from fastapi import  FastAPI
from routs import get_csv
from db.init_db import create_db_and_tables
app = FastAPI()

app.include_router(get_csv.router)





if __name__ == '__main__':
    create_db_and_tables()
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

