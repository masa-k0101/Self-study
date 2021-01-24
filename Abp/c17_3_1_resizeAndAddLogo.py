#! python3
# resizeAndAddLogo.py - カレントディレクトリのすべての画像を300x300に収まる
#                       ようにサイズ変更し、catlogo.pngを右下に追加する

import os
from PIL import Image

SQUARE_FIT_SIZE  =300
LOGO_FILENAME = 'catlogo.png'

logo_im = Image.open(LOGO_FILENAME)
logo_width, logo_height = logo_im.size

# TODO: カレントディレクトリの全画像をループする

# TODO: 画像をサイズ変更する

# TODO: ロゴを追加する

# TODO: 変更を保存する