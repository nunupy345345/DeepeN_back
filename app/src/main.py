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
    test_obj = Hira(req.word)
    result = test_obj.hira()
    return {"ひらがな": result}
    
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Error tests: {str(e)}")
    


@app.post("/fromJtoD") # 日本語→ペン語
def deepen(req:TestModel):
  try:
    print(req.word)
    test_obj = Deepen(req.word) # Deepenクラスのインスタンスを作成
    result = test_obj.translation(dictionary)
    return {"ペン語": result}
    
  except Exception as e:
    # error発生したときにHTTP Exceptionを発生
    raise HTTPException(status_code=500, detail=f"Error tests: {str(e)}")



@app.post("/fromDtoJ") # ペン語➡︎日本語
def deepen(req:TestModel):
  try:
    print(req.word)
    test_obj = R_Deepen(req.word)
    result = test_obj.r_translation(r_dictionary)
    return {"日本語": result}
    
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Error tests: {str(e)}")
  

@app.post("/deepen")   #変換方向を自動選択
def deepen(req:TestModel):
  try:
    print(req.word)
    judgeStr = req.word.replace("ぺ","").replace("ー","").replace("ン","").replace("　","")     #「ぺ、ー、ン、"　"」を除いた文字列を作成
    if judgeStr == "":      #空ならペン語 → 日本語
      test_obj = R_Deepen(req.word)
      result = test_obj.r_translation(r_dictionary)
      derection = "ペン語 → 日本語"
    else:
      test_obj = Deepen(req.word)     #空でないなら日本語 → ペン語
      result = test_obj.translation(dictionary)
      derection = "日本語 → ペン語"
    return {derection: result}
    
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Error tests: {str(e)}")