"""
def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
    weather_information = [
        {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
        {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
        {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},

        {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
        {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
        {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},

        {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
        {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
    ]

    # Q1. 全国の平均気温を計算してください(9.5となればOK)

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)

    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)


if __name__ == '__main__':
    main()
"""
weather_information = [
    {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
    {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
    {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},

    {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
    {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
    {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},

    {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
    {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
]
# Q1. 全国の平均気温を計算してください(9.5となればOK)
sum_temp = 0

for info in weather_information:
    sum_temp += info['temperature']
print(sum_temp / len(weather_information))

# Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)
station_list = []
for info in weather_information:
    if info['prefecture'] == '大阪府':
        station_list.append(info['station'])
print(','.join(station_list))

# Q3. 福岡県の平均気温を計算してください(14.0となればOK)
hukuoka_temp = []

for info in weather_information:
    if info['prefecture'] == '福岡県':
        hukuoka_temp.append(info['temperature'])
print(sum(hukuoka_temp) / len(hukuoka_temp))
