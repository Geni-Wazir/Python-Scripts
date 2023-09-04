# Python-Scripts
The repository includes several Python scripts that I developed during the initial stages of my learning journey. These scripts pertain to topics in the fields of **cybersecurity** and **automation**.


# Script Files

- Info extractor
- Folder Locker
- Hide Data
- Unhide Data
- Password changer

## Info Extractor
The Info Extractor is a Python script that operates discreetly in the background when executed on a Windows system. It gathers various data, including:
- System details
- All user accounts available
- Drive information
- List of all the installed applications
- List of all the files and folders
- All connected Wi-Fi networks along with their passwords. 

The script compiles this information into a text file, which is then sent to me via email as an attachment, providing a comprehensive overview of the system's status.


## Folder Locker

This Python script serves the purpose of securing a folder by implementing a password protection mechanism. It leverages the built-in Windows functionality to lock the selected folder, enabling users to choose the specific file they wish to secure with a password.

## Hide Data

The provided code is utilized to conceal all data within a folder, making it entirely invisible, even when the "Show Hidden Folders" option is activated. This code could also be employed for malicious purposes, as it renders the victim unable to view their own files and folders.


## Unhide Data

This piece of code is designed to reverse the modifications made by the "Hide Data" code. Its primary function is to reveal all the data within a folder and restore visibility to the user.

## Passowd Changer

The provided script is intended to modify the current user's password without their notification. The password is generated based on the user's MAC address.
The script additionally creates a standard user account with basic permissions, excluding it from the administrator group.
