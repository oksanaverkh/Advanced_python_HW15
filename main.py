# 📌 Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# 📌 Соберите информацию о содержимом в виде объектов namedtuple.
# 📌 Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# 📌 В процессе сбора сохраните данные в текстовый файл используя логирование.


import logging
import os
from collections import namedtuple
import argparse

logging.basicConfig(filename='logger.log', level=logging.NOTSET,
                    datefmt='%H:%M:%S', encoding='utf-8', format='[{levelname:<8}] {asctime}: {funcName} -> {msg}', style='{')
LOGGER = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description='parsing string to date')
parser.add_argument('-d', metavar='D', type=str,
                    help='Absolute directory path in double quotes', default='')

ObjectInDir = namedtuple('ObjectInDir', ['file_dir_name', 'extension',
                                         'is_directory', 'parent_dir_name'], defaults=['', 'Not applicable', True, ''])


def traverse_directory(directory):
    for root, dirs, files in os.walk(directory):
        for name in files:
            extension = name.split('.')[-1]
            name = name.replace('.'+extension, '')
            object = ObjectInDir(name, extension, False, root)
            LOGGER.info(f'File added correctly: {object}')

        for name in dirs:
            object = ObjectInDir(file_dir_name=name, parent_dir_name=root)
            LOGGER.info(f'Directory added correctly: {object}')


if __name__ == '__main__':
    try:
        arg = parser.parse_args()
        traverse_directory(f'{arg.d}')
    except:
        LOGGER.error('Incorrect directory path entered')
