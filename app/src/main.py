from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from services.test import Test
from models import TestModel
import random as r

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
    
@app.get("/omatu")
def omatu():
  try:
    lucks = ["皇帝ペンギン","アデリーペンギン","マカロニペンギン","ジェンツーペンギン","フィヨルドランドペンギン","キングペンギン","マゼランペンギン","リトルブルーペンギン","ロイヤルペンギン","ガラパゴスペンギン"]

    #ペンギンの一覧からランダムで選択
    luck = r.choice(lucks)
    
    #ペンギンの内容で表示する文章を変える
    if luck == "皇帝ペンギン":
       detail = {
          "property" : "忍耐強くリーダーシップに優れる",
          "result" : "あなたはリーダーシップに優れ、困難な状況でも冷静さを保つ力があるペン！今週はプロジェクトや仕事でリーダーシップを発揮する機会が訪れるでしょう。あなたの落ち着いた判断がチームを成功に導くペン！",
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

    elif luck == "フィヨルドランドペンギン":
      detail = {
        "property" : "臆病だが非常に賢い",
        "result" : "慎重で賢明なあなたは、今週もリスクを回避しながら成功への道を進むペン。情報収集に時間をかけ、賢い選択を心がけることで、大きな成功が期待できるペン！",
        "color" : "グリーン",
        "item" : "ノートパソコン",
        "day" : "月曜日",
        "trivia" : "フィヨルドランドペンギンは、ニュージーランドのフィヨルドランド地方に生息していて、その慎重な性格と知恵で知られてるペン！",
      }

    elif luck == "キングペンギン":
      detail = {
        "property" : "優雅で堂々としている",
        "result" : "優雅で堂々とした態度が評価される一週間です。仕事やプライベートでリーダーシップを発揮する場面が増え、周囲からの信頼も高まるペン。自信をもって行動するペン。",
        "color" : "ゴールド",
        "item" : "高級なペン",
        "day" : "木曜日",
        "trivia" : "キングペンギンは、皇帝ペンギンに次いで大きなペンギンで、特にその美しい羽毛と堂々とした姿勢が特徴ペン！",
      }

    elif luck == "マゼランペンギン":
      detail = {
        "property" : "家族思いで協力的",
        "result" : "家族や友人との絆が深まる一週間ペン。協力し合うことで困難を乗り越え、充実感を得るでしょう。家族との時間を大切に過ごすペン！",
        "color" : "レッド",
        "item" : "写真立て",
        "day" : "日曜日",
        "trivia" : "マゼランペンギンは、南アメリカの沿岸に生息し、家族単位で巣を作り、協力して子育てを行うペン！",
      }

    elif luck == "リトルブルーペンギン":
      detail = {
        "property" : "小さくて愛らしいが非常に勇敢",
        "result" : "小さな勇者なあなたは、どんな困難にも立ち向かう勇気を持ってるペン。今週は新しい挑戦に挑むことで、大きな成長を遂げるでしょう。自分を信じて一歩を踏み出すペン！",
        "color" : "ライトブルー",
        "item" : "小さなアクセサリー",
        "day" : "火曜日",
        "trivia" : "リトルブルーペンギンは、世界最小のペンギン種で、その小さな体にもかかわらず非常に勇敢ペン！",
      }

    elif luck == "ロイヤルペンギン":
      detail = {
        "property" : "高貴で好奇心旺盛",
        "result" : "好奇心旺盛なあなたは、新しい知識や経験を追及することで充実した日々を送るでしょう。学びの場や新しい趣味に挑戦することで、自分自身の視野を広げることができるペン。",
        "color" : "パープル",
        "item" : "本",
        "day" : "土曜日",
        "trivia" : "ロイヤルペンギンは、黄色い冠羽を持ち、その高貴な姿と好奇心旺盛な性格で知られてるペン！",
      }

    elif luck == "ガラパゴスペンギン":
      detail = {
        "property" : "適応力が高く創造的",
        "result" : "適応力の高さが光る週です。予期せぬ変化にも柔軟に対応し、新しいアイデアを生み出すことで成功に導かれるでしょう。創造力を発揮する場面が増える予感ペン！",
        "color" : "シルバー",
        "item" : "メモ帳",
        "day" : "金曜日",
        "trivia" : "ガラパゴスペンギンは、赤道直下のガラパゴス諸島に生息し、その特殊な環境に対応する能力で知られてるペン！",
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



    