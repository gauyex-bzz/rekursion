import os
import csv


def list_files(startpath):
    # Create a list to store file information
    file_list = []
    for root, dirs, files in os.walk(startpath):
        for filename in files:
            # Join the root path with the file name to get the full file path
            filepath = os.path.join(root, filename)
            # Get the size of the file in bytes
            size = os.path.getsize(filepath)
            # Append file information to the list
            file_list.append((filename, size, filepath))
    return file_list


# Path to C drive
c_drive_path = 'C:\\Program Files\Rockstar Games'

# Get list of files in C drive
files = list_files(c_drive_path)

# Write file information to a CSV file
with open('c.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')  # Set the delimiter to semicolon
    # Write header
    writer.writerow(['File Name', 'Size (bytes)', 'File Path'])
    # Write file information
    for file_info in files:
        writer.writerow(file_info)

print("File Created")
