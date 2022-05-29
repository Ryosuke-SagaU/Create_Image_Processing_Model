import json

file_name = './out.json'
class_list = {'circle':0}

with open(file_name) as f:
    # 開いたファイルから、Json 形式で展開する
    js = json.load(f)

    # Json frames から、呼び出したアイテムをループさせてるけど、k,v がどんな値をとりうるか予測できない
    for k, v in js['frames'].items():

        # ここで、取り出して代入した値を確認する
        print('k: ' + str(k) + ':' + 'v: ' + str(v))

        k = int(k)

        # Json 形式のlineを定義
        line = {}

        # .以下の形式を変換してみる(ビルドされなかったら)
        line['file'] = '{0:04d}'.format(k + 1) + '.png'

        # depthは、検知したいもしくは学習させる種類の数だと仮定する
        line['image_size'] = [{
            'width':int(v[0]['width']),
            'height':int(v[0]['height']),
            'depth':1
        }]

        # key 'image_size' で保存する valueを確認する
        print('image_size width: ' + str(v[0]['width']))
        print('image_size height: ' + str(v[0]['height']))

        # ラベリングした情報を保存するために新たにリストを作成する
        line['annotations'] = []

        for annotation in v:

            line['annotations'].append(
                {
                    'class_id':class_list[annotation['tags'][0]],
                    'top':int(annotation['y1']),
                    'left':int(annotation['x1']),
                    'width':int(annotation['x2']) - int(annotation['x1']),
                    'height':int(annotation['y2']) - int(annotation['y1'])
                }
            )

            # 構成要素の確認を行う
            print('class_id: ' + str(class_list[annotation['tags'][0]]))
            print('top: ' + str(annotation['y1']))
            print('left:' + str(annotation['x1']))
            print('width: ' + str(int(annotation['x2']) - int(annotation['x1'])))
            print('height: ' + str(int(annotation['y2']) - int(annotation['y1'])))

        # ラベリングした情報を保存するために新たにリストを作成する
        line['categories'] = []

        for name, class_id in class_list.items():

            line['categories'].append(
                {
                    'class_id':class_id,
                    'name':name
                }
            )

            # 構成要素の確認を行う
            print('class_id: ' + str(class_id))
            print('name: ' + str(name))

        # 1つずつJsonファイルとして保存している
        # w で指定すると、ファイルの新規書き込みが行われる
        f = open('./json/' + '{0:04d}'.format(k + 1) + '.json', 'w')

        # 定義したものをJson Format に対応させる
        json.dump(line, f)