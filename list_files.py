# Prints only files
import os

directory = '.'

files_and_folders = os.listdir(directory)

print("Files in current directory are:")
for x in files_and_folders:
    if os.path.isfile(os.path.join(directory, x)):
        print(x)