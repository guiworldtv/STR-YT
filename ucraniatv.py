import glob
import os

path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

if os.path.exists("lista2.m3u8"):
    os.remove("lista2.m3u8")
else:
    print("The file does not exist")

read_files = glob.glob("*.m3u8")

print(read_files)

with open("lista2.m3u8", "wb") as outfile:
    for f in read_files:
        i = 0
        line = "\n"
        i += 1
        outfile.write(line.encode('utf-8'))
        
        with open(f, "rb") as infile:
            outfile.write(infile.read())
