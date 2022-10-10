from PIL import Image
from pathlib import Path

print('''\n
*********************************************************************************************
Instructions: 

1) Make sure to move/save the file you wish to convert into the same path as this program.
2) Enter the Full file name including the extension e.g.: charmander.jpg
3) Enter the file format you wish to convert to. e.g. jpeg, png (do not include .)

*********************************************************************************************
''')

while True:
    try:
        in_File = str(
            input("Please enter the file name including file type extension: \n"))
        path_str = Path(in_File)
        if path_str.exists() == False:
            print("Input file not found, please try again.\n")
            continue
        break
    except:
        print("Error in the file name entered, please try again.\n")

while True:
    try:
        output_format = str(
            input("\nPlease enter the format you would like to convert to: e.g.: jpeg, png, etc. \n"))
        if output_format not in ["jpg", "jpeg", "png"]:
            print("Output file format not recognized, please try again.")
            continue
        break
    except:
        print("Error in the file format entered, please try again.\n")


if path_str.exists():
    out_File = in_File.split(".")[0]
    with Image.open(in_File) as img:
        try:
            img.save(out_File+"-converted."+output_format, output_format)
        except:
            print("Error, could not convert Image to specified format.\n")
    print("Conversion completed.\n")
    img.show()
else:
    print("Error, File not found.\n")
