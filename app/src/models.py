from pydantic import BaseModel
# request bodyで渡すときのモデルを作る

class TestModel(BaseModel):
  word: str