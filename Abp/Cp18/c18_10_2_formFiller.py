#! python3
# formFillerw.py - フォームの自動入入力
 
import pyautogui, time

# 以下の値は実際に調べたものに置き換えること
name_field = (648, 319)
submit_button = (651, 817)
submit_button_color = (75, 141, 249)
submit_another_link = (760, 224)

form_data = [{'name': 'Alice', 'fear': 'eavesdroppers', 'sourece': 'wand',\
              'robocop': 4, 'comments': 'Tell Bob I said hi.'},\
             {'name': 'Bob', 'fear': 'bees', 'sourece': 'amulet',\
              'robocop': 4, 'comments': 'n/a.'},\
             {'name': 'Carol', 'fear': 'puppets', 'sourece': 'crystal ball',\
              'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},\
             {'name': 'Alex Murpyh', 'fear': 'ED-209', 'sourece': 'money',\
              'robocop': 5, 'comments': 'Protect the innocent, Serve the public trust. Upload the Law.'},\
            ]

pyautogui.PAUSE = 0.5

# TODO: ユーザーがスクリプトを中断する機会を与える

# TODO: フォームページが読み込まれるのを待つ

# TODO: Name欄を入力する

# TODO: Greatest Fear(s)を入力する

# TODO: Source of Wizard Powers欄を選択する

# TODO: RoboCop欄を選択する

# TODO: Additional Comments欄を入力する

# TODO: Submitをクリックする

# TODO: 次のページが読み込まれるを待つ

# TODO: Submit anotyher responceリンクをクリックする