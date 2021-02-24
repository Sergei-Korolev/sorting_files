import os

from random import randint


PATH = './test_folder'
TYPES = [
    '.txt', '.csv', '.zip', '.exe', '.pickle', '.dat', '.bin',
    '.doc', '.docx', '.jpg', '.rar', '.zip', '.torrent', '.msi',
    '.java', '.html']


def fill_folder(path):
    """Filling 'PATH' folder with diffent TYPES of files"""
    for i in range(len(TYPES)):
        for k in range(1, randint(2, 10)):
            with open(f'{PATH}/test_file{str(k)}{TYPES[i]}', 'wb'):
                pass


if __name__ == '__main__':
    if not os.path.exists(PATH):
        os.mkdir(PATH)

    fill_folder(PATH)
