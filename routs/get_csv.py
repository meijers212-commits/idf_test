from fastapi import APIRouter, File, UploadFile
from controlers.csv_controler import convert_csv_to_matrix, create_table_from_csv


router = APIRouter(prefix="/csv", tags=["csv"])

@router.post("/assignWithCsv")
def upload_csv(file: UploadFile = File(...)):
    rows = convert_csv_to_matrix(file)
    create_table_from_csv("solders",rows)
    return  {
        "message": "CSV successfully loaded",
        "rows_count": len(rows),
        "data": rows,
    }