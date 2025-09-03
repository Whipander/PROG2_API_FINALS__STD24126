from fastapi import FastAPI
from starlette.responses import JSONResponse, Response

app = FastAPI()

@app.get('/ping')
def ping():
    return JSONResponse({'message': 'pong'}, status_code=200)

@app.get("/health")
def get_health():
    return Response(content="Ok", status_code=200)