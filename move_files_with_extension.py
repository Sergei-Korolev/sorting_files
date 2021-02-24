import os
import shutil


PATH = './test_folder/'
FILES = os.listdir(PATH)


def create_folder(extension: str):
    """Creating folder for each unique file extension
    and return extension path
    """
    extension_path = PATH + f'{extension}/'
    if extension not in os.listdir(PATH):  # os.listdir(PATH) every time calculated
        os.mkdir(extension_path)
        # print(f'Create folder for .{extension}')
    # print(f'Folder for .{extension} already exsists')
    return extension_path


def move_and_rename_file(file_name: str, extension: str):
    """Moving file to folder and rename file if file exists in this folder"""
    extension_path = create_folder(extension)
    print(extension_path)
    if file_name in os.listdir(extension_path):
        index = 1
        while file_name in os.listdir(extension_path):
            new_file_name = file_name.replace(f'.{extension}',
                                              f'{index}.{extension}')

            if new_file_name not in os.listdir(extension_path):
                os.rename(PATH + file_name, PATH + new_file_name)
                file_name = new_file_name
            index += 1

    shutil.move(PATH + file_name, extension_path + file_name)


def main():
    for f in FILES:
        if os.path.isfile(PATH + f):
            extension = f[f.rfind('.') + 1:]
            move_and_rename_file(f, extension)
            # print(f'File {f} moved to "{extension}" folder')
    print('All done')


if __name__ == '__main__':
    main()
