import sys
import os
from PIL import Image


def convert(origin_path, destination_path):
    '''
    Converts all .jpg files in a directory to .png files in another directory.

    Arguments:
    origin_path -- source directory, which contains images to convert
    destination_path -- destination directory, which will contain converted .png files
    '''
    if os.path.exists(origin_path):
        images_list = os.listdir(origin_path)
        for image_path in images_list:
            if os.path.splitext(image_path)[1] != '.jpg':
                continue
            if not os.path.exists(destination_path):
                os.mkdir(destination_path)
            image = Image.open(origin_path + image_path)
            image.save(destination_path +
                       os.path.splitext(image_path)[0] + '.png', 'png')
    else:
        print('Source directory does not exist.')


def main():
    try:
        origin_path = sys.argv[1]
        destination_path = sys.argv[2]
    except IndexError:
        print('Please input an origin directory and a destination directory.')
        exit()

    convert(origin_path, destination_path)


if __name__ == "__main__":
    main()
