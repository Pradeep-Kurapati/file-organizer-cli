# Prints both files and folders in current directory
import os

directory = '.'

files_and_folders = os.listdir(directory)

print("Folders in current directory are:")
for x in files_and_folders:
    if os.path.isdir(os.path.join(directory, x)):
        print(x)