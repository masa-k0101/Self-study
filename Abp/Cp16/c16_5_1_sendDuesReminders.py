#! python3
# -*- coding: utf-8 -*-

import openpyxl, smtplib, sys

# スプレッドシートを開き、最近の支払い状況を取得
wb = openpyxl.load_workbook('duesRecords.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')

last_col = sheet.get_highest_column()
latest_month = sheet.cell(row=1, column=last_col).value

# TODO: 会員の支払い状況を調べる
# TODO: メールアカウントにログインする
# TODO: リマインダーメールを送信する
