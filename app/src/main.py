from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from src.services.test import Test
from src.services.test import Hira
from src.services.translation import Deepen
from src.services.translation import R_Deepen
from src.models import TestModel
from src.services.dict.dictfile import dictionary
from src.services.dict.dictfile import r_dictionary
import random as r

app = FastAPI()

origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173",
    "http://localhost:8080",
    "https://deepe-n-front-64wo.vercel.app",
    "https://deepe-n-front-64wo.vercel.app/zukan"
    "https://deepen-back.onrender.com"
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
    
@app.get("/omatu")
def omatu():
  try:
    lucks = ["皇帝ペンギン","アデリーペンギン","マカロニペンギン","ジェンツーペンギン"]

    #ペンギンの一覧からランダムで選択
    luck = r.choice(lucks)
    
    #ペンギンの内容で表示する文章を変える
    if luck == "皇帝ペンギン":
       detail = {
          "property" : "特性: 忍耐強くリーダーシップに優れる",
          "result" : "占い結果: 「あなたはリーダーシップに優れ、困難な状況でも冷静さを保つ力があるペン！今週はプロジェクトや仕事でリーダーシップを発揮する機会が訪れるでしょう。あなたの落ち着いた判断がチームを成功に導くペン！」",
          "color" : "ネイビー",
          "item" : "手帳",
          "day" : "水曜日",
          "trivia" : "皇帝ペンギンは最も背の高いペンギンで、厳しい南極の冬を耐え抜くための優れた忍耐力を持ってるペン！"


       }
    elif luck == "アデリーペンギン":
       detail = {
          "property" : "活発で社交的",
          "result" : "社交的でエネルギッシュなあなたは、今週も多くの人と交流することで新しい発見や喜びを見つけるでしょう。イベントやパーティーに参加すると、素敵な出会いが待ってるペン！",
          "color" : "イエロー",
          "item" : "カフェのコーヒー",
          "day" : "金曜日",
          "trivia" : "アデリーペンギンは非常に活発で、泳ぐ速度も速いことで知られてて、彼らのエネルギッシュな性格は群れの中でも目立つペン！"
       }

    elif luck == "マカロニペンギン":
       detail = {
          "property" : "鮮やかな外見と独特のスタイル",
          "result" : "クリエイティブなアイデアが多くの人に影響を与えるでしょう。あなたの独特のセンスとスタイルが周囲を魅了するペン！",
          "color" : "オレンジ",
          "item" : "アートブック",
          "day" : "土曜日",
          "trivia" : "マカロニペンギンは、頭にある黄色い冠羽が特徴的で、そのユニークな見た目が名前の由来となってるペン！"


       }
    else:
      detail = {
        "property" : "高速で泳ぐ能力と冒険心",
            "result" : "旅行や新しい趣味を始めることで、驚くべき発見があるでしょう。冒険心が旺盛なあなたには、新しいチャンスが訪れるペン！",
            "color" : "ブルー",
            "item" : "スニーカー",
            "day" : "火曜日",
            "trivia" : "ジェンツーペンギンは、ペンギンの中でも特に速く泳ぐことができて、そのスピードは時速36キロメートルに達するペン!"


      }
    
    return {"detail": detail}
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Error omatu: {str(e)}")

    
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
    judgeStr = req.word.replace("ぺ","").replace("ー","").replace("ン","").replace("　","").replace("？","").replace(" ","").replace("\n","")    #「ぺ、ー、ン、"　"」を除いた文字列を作成
    if judgeStr == "":      #空ならペン語 → 日本語
      test_obj = R_Deepen(req.word)
      result = test_obj.r_translation(r_dictionary)
      derection = "return"
    else:
      test_obj = Deepen(req.word)     #空でないなら日本語 → ペン語
      result = test_obj.translation(dictionary)
      derection = "return"
    return {derection: result}
    
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Error tests: {str(e)}")
