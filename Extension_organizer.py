import os
import shutil
def get_valid_folder(prompt):
    # Identify the .pdf, .docx's
    
    Folder_type = {
        "Images": [".jpg", ".jpeg", ".gif", ".png", ".webp"],
        "Documents": [".pdf", ".docx"],
        "videos": [".mp4", ".mov", ".mkv", ".webm", ".avi"],}
    
    # Get users input of the wanted folder to organize
    
    user_input = input("enter the folder that you want to organize each file: ")
    
    # Strickly move them to there designated folder type like .pdf to images folder
    
    if os.path.exists(user_input) and os.path.isdir(user_input):
        return user_input
    else:
        print("Invalid try again")

    # Capture
    source_dir = get_valid_folder("Enter the path of source folder")
    dest_dir = input("Enter path for destination")
    
    # Destination

    # Shutil to copy contents

    # go through files to avoid nested folder duplication


    # if the folder doesnt exist create the folder for that type 