# -*- coding: utf-8 -*-

#! python3
# combinePdfs.py - カレントディレクトリの全PDFをひとつのPDFに結合する

import pyPDF2, os

# すべてのPDFファイル名を取得する
pdf_files = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdf_files.append(filename)

pdf_files.sort(key=str.lower)

pdf_writer = pyPDF2.PdfFileWriter()

# TODO: すべてのPDFファイルをループする

# TODO: 先頭を除くすべてのページをループして追加する

# TODO: 結合したPDFファイルに保存する
