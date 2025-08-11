# Prints both files and folders in current directory
import os

directory = '.'

files_and_folders = os.listdir(directory)

print("Files and folders in current directory are:")
for x in files_and_folders:
    if os.path.isfile(x):
        print(x)