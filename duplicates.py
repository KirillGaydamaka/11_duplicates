import os
import argparse
from collections import defaultdict


def create_parser():
    parser = argparse.ArgumentParser(description='Parameters')
    parser.add_argument('path', help='Path to folder')
    args = parser.parse_args()
    return args


def get_file_sizes(path):
    files_dict = defaultdict(list)
    for root, dirs, files in os.walk(path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_size = os.path.getsize(file_path)
            files_dict[(file_name, file_size)].append(root)
    return files_dict


def main():
    try:
        path = create_parser().path
        if not os.path.exists(path):
            print('Folder does not exist')
            return None
        if not os.path.isdir(path):
            print('Not a directory')
        files_dict = get_file_sizes(path)
    except OSError:
        print("Can't read files")
        return None

    print('Found duplicate files:')
    for filename, filesize in files_dict:
        if len(files_dict[(filename, filesize)]) > 1:
            print('--\n{} of size {} bytes in folders:'.format(filename,
                                                               filesize))
            print('\n'.join(files_dict[(filename, filesize)]))


if __name__ == '__main__':
    main()
