from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from .services.test import Test
from .models import TestModel

app = FastAPI()

origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173",
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def hello_world():
    return {"message": "Hello World"}
  
@app.get("/test")
def test():
  return {"message" : "test"}

@app.post("/test")
def test(req:TestModel):
  try:
    print(req.word)
    test_obj = Test(req.word) # Testクラスのインスタンスを作成
    result = test_obj.test()
    return {"result": result}
    
  except Exception as e:
    # error発生したときにHTTP Exceptionを発生
    raise HTTPException(status_code=500, detail=f"Error tests: {str(e)}")
    