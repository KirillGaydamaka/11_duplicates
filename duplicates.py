import os
import argparse


def create_parser():
    parser = argparse.ArgumentParser(description='Parameters')
    parser.add_argument('path', help='Path to folder')
    args = parser.parse_args()
    return args


def get_file_sizes(path):
    file_sizes_list = []
    for root, dirs, files in os.walk(path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_size = os.path.getsize(file_path)
            file_sizes_list.append((file_name, file_size))
    return file_sizes_list


def main():

    try:
        path = create_parser().path
        if not os.path.exists(path):
            print('Folder does not exist')
            return None
        if not os.path.isdir(path):
            print('Not a directory')
            return None
        file_sizes_list = get_file_sizes(path)
        duplicates_set = set([x for x in file_sizes_list if file_sizes_list.count(x) > 1])
        print('Duplicate files:')
        for filename, filesize in duplicates_set:
            print(filename, 'of size', filesize, 'bytes')
    except OSError:
        print("Can't read files")


if __name__ == '__main__':
    main()
