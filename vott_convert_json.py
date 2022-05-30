import os
from glob import glob

def change_json_file_name():

    # json/new_json_data 以下のファイルをリストとして出力する
    print(glob('json/new_json_data/*'))

    path = "json/new_json_data"
    raw_json_list = glob(path + '/*')

    # os.rename('変更前のファイル名', '変更後のファイル名')
    for i, f in enumerate(raw_json_list, 1):
        root, ext = os.path.splitext(f)
        os.rename(f, os.path.join(path, '{0:04d}').format(i) + ext)