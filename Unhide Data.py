import os
import subprocess

directory = []
files = []
drives = ["d://", "e://"]


def to_get_all_directories():
    for i in drives:
        os.chdir(i)
        a = subprocess.getoutput("dir *.* /S /p")  # to get the output of the command that search the
        # files in a particular directory
        b = a.split("\n\n")  # to split the result according to the given instruction
        for k in b:
            if " Directory of " in k:
                directory.append(k[14:])   # take the path of the directories from the result


to_get_all_directories()

for data in directory:
    files.append(os.listdir(data))   # getting the files present in the directories captured above having some extension


def execution_of_program():
    a = 0
    for p in directory:
        n = 0
        for s in range(len(files[a])):
            try1 = "attrib -h  -s -r " + p + "\\" + files[a][n]  # joining the path of the directory and the name
            # of the files together to get the location of the data
            subprocess.call(str(try1), shell=True)
            n += 1
        subprocess.call(str("attrib -h  -s -r " + p), shell=True)
        a = a+1


execution_of_program()

info = open("HACKED.txt", "w+")   # creating a new file in that directory
info.write("\t\t\t\t\tEVERYTHING IS FINE \n\n\n\t\t\t\t\tPLEASE CHECK YOUR DATA")   # giving input to the text file
info.close()
os.startfile("HACKED.txt")
