from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from services.test import Test
from services.test import Hira
from services.translation import Deepen
from services.translation import R_Deepen
from models import TestModel
from services.dict.dictfile import dictionary
from services.dict.dictfile import r_dictionary


app = FastAPI()



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
  

    
@app.post("/hiragana") # ひらがな
def hiragana(req:TestModel):
  try:
    print(req.word)
    test_obj = Hira(req.word) # Hiraクラスのインスタンスを作成
    result = test_obj.hira()
    return {"ひらがな": result}
    
  except Exception as e:
    # error発生したときにHTTP Exceptionを発生
    raise HTTPException(status_code=500, detail=f"Error tests: {str(e)}")
    


@app.post("/deepen") # ペン語
def deepen(req:TestModel):
  try:
    print(req.word)
    test_obj = Deepen(req.word) # Deepenクラスのインスタンスを作成
    result = test_obj.translation(dictionary)
    return {"ペン語": result}
    
  except Exception as e:
    # error発生したときにHTTP Exceptionを発生
    raise HTTPException(status_code=500, detail=f"Error tests: {str(e)}")

@app.post("/r_deepen") # ペン語
def deepen(req:TestModel):
  try:
    print(req.word)
    test_obj = R_Deepen(req.word) # Deepenクラスのインスタンスを作成
    result = test_obj.r_translation(r_dictionary)
    return {"ペン語": result}
    
  except Exception as e:
    # error発生したときにHTTP Exceptionを発生
    raise HTTPException(status_code=500, detail=f"Error tests: {str(e)}")