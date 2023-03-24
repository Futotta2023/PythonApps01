import random

# 名前を入力させる
name = input("あなたの名前を入力してください: ")

# 運勢のリスト
fortunes1 = ["大吉", "中吉", "小吉", "末吉", "凶"]
fortunes2 = ["Dikichi", "Cyukichi", "Shokichi", "Suekichi", "Kyo"]

# 名前が英語の場合は英語で運勢を表示、それ以外は日本語で表示
if name.isalpha() and name.isascii():
    # ランダムに運勢を選択し、英語で表示
    fortune = random.choice(fortunes2)
    print("Your fortune is {}.".format(fortune))
else:
    # 名前の文字数を取得
    name_length = len(name)
    # ランダムに運勢を選択し、日本語で表示
    fortune = random.choice(fortunes1)
    print("{}さんの運勢は{}です。".format(name, fortune))
