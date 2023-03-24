import datetime


def validate_date(year: int, month: int, day: int) -> None:
    try:
        datetime.datetime(year, month, day)
    except ValueError:
        raise ValueError("無効な日付")


def convert_japanese_era_to_ad(japanese_era: str, year: int) -> int:
    # 和暦から西暦への変換辞書
    era_dict = {
        "明治": (1868, 1, 1),
        "大正": (1912, 7, 30),
        "昭和": (1926, 12, 25),
        "平成": (1989, 1, 8),
        "令和": (2019, 5, 1)
    }

    # 和暦が辞書にない場合はエラーを返す
    if japanese_era not in era_dict:
        raise ValueError("こんな和暦はありませんよ")

    # 和暦から西暦への変換
    ad_year, month, day = era_dict[japanese_era]
    ad_year += year - 1

    # 変換した西暦が存在するか確認するgit --version
    validate_date(ad_year, month, day)

    return ad_year


# 和暦を西暦に変換するための関数呼び出し
japanese_era = input("知りたい和暦を入力してください")
year = int(input("知りたい年数を入力してください"))
try:
    ad_year = convert_japanese_era_to_ad(japanese_era, year)
    print(f"{japanese_era}{year}年は西暦{ad_year}年です。")
except ValueError as e:
    print(e)
