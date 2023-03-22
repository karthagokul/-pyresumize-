from pyresumizer import ResumeProcessor

from os import path
from glob import glob

def find_ext(dr, ext):
    return glob(path.join(dr, "*." + ext))
r_parser=ResumeProcessor()
#Lets find the files from a folder of .pdf extension
files=find_ext(".test_data","pdf")
for file in files:
    print("Parsing " + file)
    json=r_parser.process_resume(file)
    print(json)
    print("")
