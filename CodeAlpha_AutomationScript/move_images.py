# -------- JPG File Automation Script --------

import os
import shutil

source_folder = input("Enter source folder path: ")
destination_folder = input("Enter destination folder path: ")

# create destination folder if not exists
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

files = os.listdir(source_folder)

count = 0

for file in files:
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
        shutil.move(os.path.join(source_folder, file),
                    os.path.join(destination_folder, file))
        count += 1

print(f"{count} image file(s) moved successfully!")
