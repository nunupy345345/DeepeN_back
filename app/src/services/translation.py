from pykakasi import kakasi 

 # 日本語→ペン語
class Deepen():
  def __init__(self, in_word) -> None:
    self.kakasi = kakasi()
    self.in_word = in_word

  def translation(self, dict) -> str:
    result = self.kakasi.convert(self.in_word)
    hiraSentence = ""
    out_pen = ""

    for i in result:
      hiraSentence += i['hira']
    List = list(hiraSentence)
    for i in List:
      out_pen += dict.get(i,"?") + "　"
    out_pen = out_pen.rstrip()
    return out_pen

#ペン語→日本語
class R_Deepen():
  def __init__(self, in_word) -> None:
    self.in_word = in_word

  def r_translation(self, dict) -> str:
    out_pen = ""
    while "　　" in self.in_word:   #二つ以上ならぶ空白にも対応
      self.in_word = self.in_word.replace("　　","　")
    self.in_word = self.in_word.strip()    #前後の空白を削除
    List = self.in_word.split("　")
    for i in List:
      out_pen += dict.get(i,"?")
    return out_pen