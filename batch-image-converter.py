from genericpath import isdir
import sys
import os
import webbrowser
from PIL import Image
from functools import reduce


def makeStringFromList(acc, portion):
    if acc != "":
        return acc+"."+portion
    else:
        return portion


def getFileCount(acc, filename):
    if filename.split(".")[-1] == "jpg":
        return acc+1
    else:
        return acc


try:
    source_folder = sys.argv[1]
    out_folder = sys.argv[2]
except:
    print("Source folder name/Output Folder name not found, please restart and enter two input parameters.")
    exit()

if os.path.isdir(source_folder) == False:
    print("Input folder does not exist, make sure the folder containing images to be converted is in the same folder as this python script.")
    exit()

if os.path.isdir(out_folder):
    print('''Output folder already exists, please backup folder to another location or delete the folder and restart.
Alternatively, choose a different name for the output folder.''')
    exit()

print("Analyzing...\n")

file_count = reduce(getFileCount, os.listdir(source_folder), 0)

if file_count == 0:
    print("No .jpg Image files were found. Program will exit now.")
    exit()

counter = 0

for file in os.listdir(source_folder):  # file incorporates full input file name
    if file.split(".")[-1] == "jpg":
        with Image.open(source_folder+"/"+file) as img:
            # makes the folder if it doesn't exist
            if os.path.isdir(out_folder) == False:
                os.mkdir(out_folder)

            file_name = reduce(makeStringFromList, file.split(".")[0:-1], "")

            img.save(out_folder+"/"+file_name+".png", "png")
            counter += 1
            print(f"Progress: {counter}/{file_count} files converted")

print("\nAll Done!")
webbrowser.open(out_folder)
