import os
import shutil

def organize_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            ext = filename.split('.')[-1].lower()
            folder = os.path.join(folder_path, ext)
            os.makedirs(folder, exist_ok=True)
            shutil.move(file_path, os.path.join(folder, filename))

if __name__ == "__main__":
    folder = input("Enter the folder path to organize: ")
    organize_files(folder)
    print("✅ Files organized successfully!")
