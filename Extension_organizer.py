import os
import shutil

# Identify the .pdf, .docx's
    
Folder_type = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".tiff", ".svg", ".ico"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".rtf", ".odt", ".md"],
    "Videos": [".mp4", ".mov", ".mkv", ".avi", ".webm", ".flv", ".wmv"],
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
    "Spreadsheets": [".xlsx", ".xls", ".csv", ".ods"],
    "Presentations": [".pptx", ".ppt", ".odp"],
    "Code": [".py", ".html", ".css", ".js", ".cpp", ".java", ".json", ".xml", ".sh", ".bat"],
    "Executables": [".exe", ".msi", ".apk", ".dmg", ".iso"],
    "Design": [".psd", ".ai", ".xd", ".blend", ".obj", ".stl"]
}

    # Get users input of the wanted folder to organize
def get_valid_directory():

    while True:    
        user_input = input("enter the folder that you want to organize each file: ")

        user_input = user_input.strip()       
        user_input = user_input.strip('\'"')  

        if os.path.isdir(user_input):
            return user_input
        else:
            print("Invalid try again")

# Get target directory
def organize_files():
    target_dir = get_valid_directory()
# Go through every file in the folder
    for filename in os.listdir(target_dir):
    # path to the file
        file_path = os.path.join(target_dir, filename)
    # If there is a duplication skip the item
        if os.path.isdir(file_path):
            continue
    # Take the file type (.jpg, .pdf) by spliting the text
    _, file_extension = os.path.splitext(filename)
    file_extension = file_extension.lower()

    # Check to see which folder it belongs to
    destination_folder_name = None
    for folder, extensions in Folder_type.items():
        if file_extension in extensions:
            destination_folder_name = folder
            break # Stop
        
        if destination_folder_name:
            dest_folder_path = os.path.join(target_dir, destination_folder_name)
            
        # If it doesnt exist
        if not os.path.exists:
            print("Invalide")
        
        # If it does
    shutil.move(file_path, os.path.join(dest_folder_path, filename))
    print(f"moved: {filename} to {dest_folder_path}/")

# Run the script
if __name__ == "__main__":
    organize_files()