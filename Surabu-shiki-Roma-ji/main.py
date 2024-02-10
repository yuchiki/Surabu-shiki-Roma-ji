import MeCab

wakati: int = MeCab.Tagger("-Owakati")
text = "あらゆる現実を自分の方に捻じ曲げたのだ。"
text2 = "hoge"
data = wakati.parse(text)

print(text)
print(data)
