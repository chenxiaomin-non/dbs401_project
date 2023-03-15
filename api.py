from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
import db_call

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    with open("./static/index.html", "r") as f:
        return Response(content=f.read(), media_type="text/html")


@app.get("/img/{file_path}")
def read_img(file_path: str):
    with open("./static/img/" + file_path, "rb") as f:
        return Response(content=f.read(), media_type="img")


@app.get("/font/{file_path}")
def read_font(file_path: str):
    with open("./static/font/" + file_path, "rb") as f:
        return Response(content=f.read(), media_type="font")


@app.get("/api/v1/students/{id}")
def get_student(id: str) -> dict:
    try:
        result: list = db_call.get_student(id)
        return {"status": "OK", "len": len(result), "data": result}
    except Exception as e:
        return {"status": "ERR", "len": 0, "data": []}


@app.get("/api/v1/test/{id}")
def get_test(id: str) -> dict:
    return {"status": "OK", "len": 1, "data": [{"id": id, "name": "test", "gpa": 9.9, "course": "MLN111"}]}
