from pykakasi import kakasi 

 # ペン語に翻訳
class Deepen():
  def __init__(self, in_word) -> None:
    self.kakasi = kakasi()
    self.in_word = in_word

  def translation(self, dict) -> list:
    result = self.kakasi.convert(self.in_word)
    hiraSentence = ""
    out_pen = ""

    for i in result:
      hiraSentence += i['hira']
    List = list(hiraSentence)
    for i in List:
      out_pen += dict.get(i,"?") + "　"
    
    return out_pen


class R_Deepen():
  def __init__(self, in_word) -> None:
    self.in_word = in_word

  def r_translation(self, dict) -> list:
    out_pen = ""
    List = self.in_word.split("　")
    for i in List:
      out_pen += dict.get(i,"?")
    return out_pen