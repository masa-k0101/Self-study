#! python3
# textmyself.py - 引数の文字列をSMSで送信するtextmyself()を定義する
# -*- coding: utf-8 -*-

# 設定値
account_SID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'
twilio_number = '+12345678901'
my_number = '+819012345678'

from twilio.rest import Client

def textmyself(message):
    twilio_cli = Client(account_SID, auth_token)
    twilio_cli.message.create(body=message, from_=twilio_number, to=my_number)