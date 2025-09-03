from fastapi import FastAPI
from starlette.responses import JSONResponse, Response
from pydantic import BaseModel
from typing import List
app = FastAPI()

@app.get('/ping')
def ping():
    return JSONResponse({'message': 'pong'}, status_code=200)

@app.get("/health")
def get_health():
    return Response(content="Ok", status_code=200)

class Characteristic(BaseModel):
    ram_memory: int
    rom_memory: int

class Phone(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristic

phone_stored: List[Phone] = []

def serialize_phone():
    serialized_phone = []
    for phone in phone_stored:
        serialized_phone.append(phone.model_dump())

    return serialized_phone
@app.post("/phones")
def add_phone(phone_to_add: List[Phone]):
    for phone in phone_to_add:
        phone_stored.append(phone)

    return JSONResponse(content=serialize_phone(), status_code=201)

@app.get("/phones")
def get_phones():
    return JSONResponse(content=serialize_phone(), status_code=200)

@app.get("/phones/{id}")
def get_phone_by_id(id: str):
   for phone in phone_stored:
       if phone.identifier == id:
           return JSONResponse(content=phone.model_dump(), status_code=200)

   return JSONResponse(content={"error": "Not found"}, status_code=404)