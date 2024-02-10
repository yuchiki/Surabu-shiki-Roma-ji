"""MeCabを使って分かち書きを行うサンプルコードです."""

import MeCab  # type: ignore[import-untyped]

if __name__ == "__main__":
    wakati = MeCab.Tagger("-Owakati")
    text = "あらゆる現実を自分の方に捻じ曲げたのだ。"
    data = wakati.parse(text)

    print(text)  # noqa: T201
    print(data)  # noqa: T201
