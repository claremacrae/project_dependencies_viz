from __future__ import print_function

from glob import glob
import os


def process_files():
    for dot_file in glob('*.dot*'):
        print(dot_file)
        convert_dot_file_to_svg(dot_file)
        break



def convert_dot_file_to_svg(dot_file):
    svg_file = os.path.splitext(dot_file)[0] + '.svg'
    command = f'dot -Tsvg {dot_file} -o {svg_file}'
    os.system(command)


if __name__ == '__main__':
    process_files()
