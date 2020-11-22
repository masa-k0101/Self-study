# -*- coding: utf-8 -*-

#! python3
# backupToZip.py - フォルダ全体を連番付きZIPファイルにコピーする

import zipfile, os

def backup_to_zip(folder):
    # フォルダ全体をZIPファイルにバックアップする

    folder = os.path.abspath(folder)

    # 既存のファイル名からファイル名の連番を決める
    number = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number = number + 1
    
    # ZIPファイルを作成する
    print('Creating {}...'.format(zip_filename))
    backup_zip = zipfile.ZipFile(zip_filename, 'w')

    # TODO: フォルダのツリーを渡り歩いてその中のファイルを圧縮する
    print('Done')

backup_to_zip('c:\\Study\\python\\Automate the Boring Stuff with Python')