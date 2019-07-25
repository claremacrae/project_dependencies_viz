from __future__ import print_function

from glob import glob
import os


def process_files():
    for dot_file in glob('*.dot*'):
        print(dot_file)
        convert_dot_file_to_svg(dot_file)


def convert_dot_file_to_svg(dot_file):
    convert_dot_file_to_image(dot_file, 'svg')


def convert_dot_file_to_image(dot_file, format):
    output_file = os.path.splitext(dot_file)[0] + '.' + format
    # This uses a Python 3 feature - f-strings, for convenience.
    # https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python
    command = f'dot -T{format} {dot_file} -o {output_file}'
    os.system(command)


if __name__ == '__main__':
    process_files()
