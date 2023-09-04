import os
import getpass
import time
import subprocess

print("DIRECT US TO YOUR FOLDER \n\n")
location = input("[+] please specify the drive: ")
location += "://"
while True:
    print("\n\n\t\t\tYOU ARE IN ", location.upper())
    print("\t\t----------------------------")
    sl = 0
    os.chdir(location)  # change the directory
    folders = os.listdir(location)   # list all the files of the present directory

    folders.sort()

    for sub_folders in folders:
        print("[" + str(sl) + "]", sub_folders)  # print all the folders  with serial no.
        sl += 1
    print("\n[*] PRESS * WHEN YOU ARE IN THE DESIRED FOLDER")
    file_no = input("\n[+] File number: ")
    if file_no == "*":  # terminate the loop if the user is in desired folder
        break
    elif int(file_no) <= sl:
        location += folders[int(file_no)] + "//"    # change the directory to navigate to the desire folder
    else:
        print("[!] Invalid file number")

directory = os.listdir(os.getcwd())  # to list all the files

print("[*] YOUR PASSWORD WILL NOT BE VISIBLE !!!!!!")
global password
for l in range(5):

    password = getpass.getpass(prompt="[+] PASSWORD: ")   # get the password
    conf = getpass.getpass(prompt="[+] CONFIRM YOUR PASSWORD: ")  # confirm password
    if password == conf:  # confirm whether the password matches with confirm password or not
        break
    else:
        print("[!] Password did't matched ")


confirm = input("\n[+] Are you sure [y/n]: ")


code1 = '''
cls

@ECHO OFF

title Folder Locker

if EXIST "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" goto UNLOCK

if NOT EXIST Locker goto MD_LOCKER

:LOCK

ren Locker "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"

attrib +h +s "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"

echo Locker get locked

goto End

:UNLOCK

echo Enter password to Unlock the LOCKER

set/p "pass=>"

'''

code2 = 'if NOT %pass%=={} goto FAIL'.format(password)

code3 = '''

attrib -h -s "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"

ren "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" Locker

echo Locker Unlocked successfully

goto End

:FAIL

echo .

echo Invalid password

echo .

goto UNLOCK

:MD_LOCKER

md Locker

echo Locker created successfully

goto End

:End
'''

if confirm == "y" or confirm == "Y":

    code = code1 + code2 + code3  # code which will lock the folder
    locker = open("key.bat", "w+")  # create a batch file
    locker.write(code)  # writing the code in the batch file
    locker.close()
    os.startfile("key.bat")  # starting the batch file to lock the folder
    print("\nPLEASE WAIT ...............", end='')
    time.sleep(2)
    print("\rENCRYPTING YOUR DATA .....................")
    time.sleep(2)

    print('\n\t\t\tPERCENTAGE COMPLETED')
    print('\t\t------------------------------')
    count = 0
    for file in directory:
        command = 'move "' + file + '" Locker'
        subprocess.run(command, shell=True, capture_output=False, check=False)

        # moving all the files to a new folder named Locker

        s = 100 // len(folders)
        for k in range(s):
            count += 1
            print("\r", count, "%", "<<", "=" * ((count // 10) * 3), " " * (30 - ((count // 10) * 3)), ">>", end='')
            time.sleep(0.01)  # printing the progress
    p = count + (100 - count)
    print("\r", p, "%", "<<", "=" * 30, " >>")
    os.startfile("key.bat")  # locking the folder named Locker
    print("\n[#] YOUR DATA HAS BEEN ENCRYPTED ")
    time.sleep(3)

note = open("note.txt", "w+")  # creating a new text file
info = '''
                             A NEW FILE NAMED ' KEY ' HAS BEEN CREATED IN THE FOLDER " {} "

                                             DO NOT DELETE IT !!!!!!!

                              THAT IS THE ONLY WAY TO GET YOUR DATA

PROCEDURE TO UNLOCK THE LOCKER :------

[1] DOUBLE CLICK ON THE FILE THAT HAS BEEN CREATED IN THE FOLDER NAMED " KEY "
[2] A PROMPT WILL APPEAR ASKING THE PASSWORD
[3] ENTER THE CORRECT PASSWORD WHICH YOU HAVE ENTERED WHILE LOCKING THE FOLDER
[4] AFTER THE SUCCESS FULL LOGIN A NEW FOLDER NAMED LOCKER WILL APPEAR
[5] ALL YOUR DATA WILL BE IN THAT LOCKER FOLDER
[6] AFTER THE USE DOUBLE CLICK ON THE ' KEY ' FILE TO LOCK YOUR LOCKER AGAIN.
                 '''.format(location.upper())
note.write(info)  # writing the note in the text file for retrieving the data back
note.close()
os.startfile("note.txt")  # starting the text file having note
