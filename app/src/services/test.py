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
    # out_word = self.kakasi.convert(self.in_word)

    result = self.kakasi.convert(self.in_word)
    out_word = ""
    PenLanguage = ""
    dict = {
      "あ":"",
      "い":"",
      "う":"",
      "a":"トン ツー"
    }
    for converted_word in result:
      out_word += converted_word['hira']
    List = list(out_word)
    for i in List:
      PenLanguage += dict.get(i,"?")
    
    return PenLanguage