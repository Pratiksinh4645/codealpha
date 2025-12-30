# Image File Automation Script (Python)

## Description

This Python script automatically moves all **.jpg / .jpeg / .png** image
files from a source folder to a destination folder. It is useful for
daily file management and simple automation tasks.

## Features

-   Automatically moves all image files
-   Creates destination folder if it does not exist
-   Shows total files moved
-   Beginner‑friendly Python program

## Technologies Used

-   Python
-   os module
-   shutil module

## How to Run

1.  Install Python
2.  Save the script as `move_images.py`
3.  Open Terminal or PowerShell
4.  Navigate to the folder where the script is saved:

```{=html}
<!-- -->
```
    cd path oolder

5.  Run the script:

```{=html}
<!-- -->
```
    python move_images.py

## Example Paths (Windows)

    Enter source: C:\Users\prath\Pictures
    Enter destination: C:\Users\prath\Desktop\ImagesMoved

## Python Code

``` python
import os
import shutil

source_folder = input("Enter source folder path: ")
destination_folder = input("Enter destination folder path: ")

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
```

## Output

-   All image files will be moved to the new folder
-   Displays total number of files moved

## Author
Pratik 