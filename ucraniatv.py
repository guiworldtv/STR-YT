import glob
import os

path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

if os.path.exists("concatenate_texts.txt"):
    os.remove("concatenate_texts.txt")
else:
    print("The file does not exist")

read_files = glob.glob("*.txt")

print(read_files)

with open("concatenate_texts.txt", "wb") as outfile:
    for f in read_files:
        i = 0
        line = "\n"
        i += 1
        outfile.write(line.encode('utf-8'))
        
        with open(f, "rb") as infile:
            outfile.write(infile.read())
