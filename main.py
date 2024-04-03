import os
import csv


def list_files(startpath):
    file_list = []
    for root, dirs, files in os.walk(startpath):
        for filename in files:
            filepath = os.path.join(root, filename)
            size = os.path.getsize(filepath)
            file_list.append((filepath, size, filename))
    return file_list


def quicksort(file_list):
    for i in range(len(file_list)):
        pivot = (file_list[i])
        left = []
        right = []
        equal = []

        for filename in file_list:
            if filename < pivot:
                left.append(filename)
            elif filename > pivot:
                right.append(filename)
            elif filename == pivot:
                equal.append(filename)
            file_list = left + equal + right
        return file_list


def main():
    c_drive_path = 'C:\\Program Files\Rockstar Games'

    files = list_files(c_drive_path)

    with open('c.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(['File Name', 'Size (bytes)', 'File Path'])
        for file_info in files:
            writer.writerow(file_info)

    print("File Created")
