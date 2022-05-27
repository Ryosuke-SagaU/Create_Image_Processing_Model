import os
from PIL import Image, ImageFilter

def main():

    data_dir_pass = 'C:\\Users\\Ryosuke Nikushi\\PycharmProjects\\model_demo\\circle_image\\out'
    data_dir_pass_in = 'C:\\Users\\Ryosuke Nikushi\\PycharmProjects\\model_demo\\circle_image\\in'
    file_list = os.listdir('C:\\Users\\Ryosuke Nikushi\\PycharmProjects\\model_demo\\circle_image\\in')

    count: int = 1
    for file_name in file_list:
        root, ext = os.path.splitext(file_name)
        if ext == '.png' or '.jpeg' or '.jpg':

            # 画像を読み込んで、変換して、変換した画像を保存する。で、カウントを増大させる
            img = Image.open(data_dir_pass_in + '/' + file_name)
            tmp = img.transpose(Image.FLIP_LEFT_RIGHT)
            tmp.save(data_dir_pass + '/' + '{0:04d}'.format(count) + '.png')
            count += 1

            # 以下似た処理を続ける。本質的に処理の流れは同じことをやっている
            #2
            tmp = img.transpose(Image.FLIP_TOP_BOTTOM)
            tmp.save(data_dir_pass + '/' + '{0:04d}'.format(count) + '.png')
            count += 1

            #3
            tmp = img.transpose(Image.ROTATE_90)
            tmp.save(data_dir_pass + '/' + '{0:04d}'.format(count) + '.png')
            count += 1

            #4
            tmp = img.transpose(Image.ROTATE_180)
            tmp.save(data_dir_pass + '/' + '{0:04d}'.format(count) + '.png')
            count += 1

            #5
            tmp = img.transpose(Image.ROTATE_270)
            tmp.save(data_dir_pass + '/' + '{0:04d}'.format(count) + '.png')
            count += 1

            #6
            tmp = img.rotate(15)
            tmp.save(data_dir_pass + '/' + '{0:04d}'.format(count) + '.png')
            count += 1

            #7
            tmp = img.rotate(75)
            tmp.save(data_dir_pass + '/' + '{0:04d}'.format(count) + '.png')
            count += 1

            #8
            tmp = img.rotate(135)
            tmp.save(data_dir_pass + '/' + '{0:04d}'.format(count) + '.png')
            count += 1

            #9
            tmp = img.rotate(195)
            tmp.save(data_dir_pass + '/' + '{0:04d}'.format(count) + '.png')
            count += 1

            #10
            tmp = img.rotate(255)
            tmp.save(data_dir_pass + '/' + '{0:04d}'.format(count) + '.png')
            count += 1