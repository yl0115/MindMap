from PIL import Image
import os


def demo():
    name = r'c:\Users\yd002\Desktop\2019.8.15'
    dirname = os.listdir(name)
    for i in dirname:
        im = Image.open(name + '\\' + i, 'r')
        im.save(i, 'png')


demo()