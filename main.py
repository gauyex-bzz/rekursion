import os
import csv


def list_files(startpath, extension=None):
    file_list = []
    for root, dirs, files in os.walk(startpath):
        for filename in files:
            if filename.endswith(extension):
                filepath = os.path.join(root, filename)
                size = os.path.getsize(filepath)
                file_list.append((filepath, size, filename))
    return file_list


def quicksort(file_list):
    if len(file_list) <= 1:
        return file_list
    else:
        pivot = file_list[len(file_list) // 2]
        left = []
        right = []
        equal = []

        for filename in file_list:
            if filename < pivot:
                left.append(filename)
            elif filename > pivot:
                right.append(filename)
            else:
                equal.append(filename)

        return quicksort(left) + equal + quicksort(right)


def main():
    c_drive_path = 'C:\\Program Files\Rockstar Games'
    extension = input("Enter the file extension (e.g., .docx, .txt): ")
    files = list_files(c_drive_path, extension)

    file_list = quicksort(files)

    with open('c.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(['File Name', 'Size (bytes)', 'File Path'])
        for file_info in files:
            writer.writerow(file_info)

    print("File Created")


if __name__ == "__main__":
    main()
