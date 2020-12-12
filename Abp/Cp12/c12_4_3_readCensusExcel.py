# -*- coding: utf-8 -*-

#! python3
# readCensusExcel.py - 郡ごとの人口調査標準地域の数を集計する

import openpyxl, pprint
print('ワークブックを開いています...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Cesus Tract')
country_data = {}

# TODO: # country_dataに郡の人口と地域数を格納する
print('行を読み込んでいます...')
for row in range(2, sheet.max_row + 1):
    # スプレッドシートの1行に、ひとつの人口調査標準地域のデータがある
    state = sheet['B' + str(row)].value
    country = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # この州のキーが確実に存在する
    country_data.setdefault(state, {})
    # この州のこの郡のキーが確実に存在するようにする
    country_data[state].setdefault(country, {'tracts': 0, 'pop': 0})

    # 各行が人口調査標準地域を表すので、数を1つ増やす
    country_data[state][country]['tracts'] += 1
    # この人口調査標準地域の人口だけ郡の人口を増やす
    country_data[state][country]['pop'] += int(pop)

# 新しいテキストファイルを開き、country_dataの内容を書き込む
print('結果を書き込み中...')
result_file = open('census2010.py', 'w')
result_file.write('all_data = ' + pprint.pformat(country_data))
result_file.close()
print('完了')