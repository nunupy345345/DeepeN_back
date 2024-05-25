from pykakasi import kakasi 
from dict.dictfile import dictionary

 # ペン語に翻訳
class Deepen():
  def __init__(self, in_word) -> None:
    self.kakasi = kakasi()
    self.in_word = in_word

  def translation(self) -> list:
    result = self.kakasi.convert(self.in_word)
    hiraSentence = ""
    out_pen = ""

    for i in result:
      hiraSentence += i['hira']
    List = list(hiraSentence)
    for i in List:
      out_pen += dictionary.get(i,"?") + "　"
    
    return out_pen
