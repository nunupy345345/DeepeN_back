from pykakasi import kakasi

class Test:
  """
  Test: pykakasiのテスト用class
  (classで管理するとすっきりするよ～)
  """
  #初期化関数
  def __init__(self, in_word) -> None:
    self.kakasi = kakasi()  # kakasi()を呼び出してオブジェクトを作成
    self.in_word = in_word  # 変換する文字列を保持
    
  # test要
  def test(self) -> list:
    """
    description: 入れられた文字列をkakashiを用いて返す
    -----------------
    in_word: str -> 変換する前の文字
    -----------------
    return out_word: list -> 変換した後のlist
    """
    out_word = self.kakasi.convert(self.in_word)
    return out_word


  #ひらがなに変換
class Hira:
  def __init__(self, in_word) -> None:
    self.kakasi = kakasi()
    self.in_word = in_word

  def hira(self) -> list:
    result = self.kakasi.convert(self.in_word)
    out_hira = ""
    for i in result:
      out_hira += i["hira"]
    return out_hira



  # ペン語に翻訳
class Deepen():
  def __init__(self, in_word) -> None:
    self.kakasi = kakasi()
    self.in_word = in_word

  def translation(self,dict) -> list:
    result = self.kakasi.convert(self.in_word)
    hiraSentence = ""
    out_pen = ""

    for i in result:
      hiraSentence += i['hira']
    List = list(hiraSentence)
    for i in List:
      out_pen += dict.get(i,"?") + "　"
    
    return out_pen
  

  # class Deepen():
  #   def __init__(self, in_word) -> None:
  #     self.kakasi = kakasi()
  #     self.in_word = in_word

  #   def translation(self,dict) -> list:
      
  #     result = self.kakasi.convert(self.in_word)
  #     out_pen = ""
  #     List = []         #直接ひらがなのリストを作りたい

  #     for i in result:
  #       List.append(i['hira'])
  #     for i in List:
  #       out_pen += dict.get(i,"?") + "　"
      
  #     return out_pen
    