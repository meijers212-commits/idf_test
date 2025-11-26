import uvicorn
from fastapi import  FastAPI
from routs import get_csv
from db.init_db import create_db_and_tables
from controlers.assining import init_dorms

app = FastAPI()
create_db_and_tables()
init_dorms()

app.include_router(get_csv.router)





if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

