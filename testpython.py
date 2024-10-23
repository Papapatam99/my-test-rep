#!/usr/bin/python3.12

import os

def get_size(path):
    size = 0
    if os.path.isfile(path):
        size = os.path.getsize(path)
    else:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                curr_file = os.path.join(dirpath, filename)
                if os.path.isfile(curr_file):
                    size += os.path.getsize(curr_file)

    return size

def human_view_size(size):
    for unit in['B','KB','MB','GB']:
        if size < 1024:
            break
        size /= 1024
    return "{:.1f}{}".format(size,unit)

def main():
    directory = os.getcwd()
    items = os.listdir(directory)
    size_list = []

    for item in items:
        full_path = os.path.join(directory, item)
        size_file = get_size(full_path)
        size_list.append((size_file, item))

    size_list.sort(key=lambda x: x[0], reverse=True)
    for size, item in size_list:
        print("{} {}".format(human_view_size(size), item))

if __name__ == "__main__":
    main()
