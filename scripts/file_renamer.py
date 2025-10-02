import os

def rename_files(folder_path, prefix="file", extension=None):
    """
    Rename all files in a folder with a given prefix.
    
    :param folder_path: Path to the folder containing files
    :param prefix: New prefix for renamed files
    :param extension: (Optional) Only rename files with this extension (e.g., '.txt')
    """
    files = os.listdir(folder_path)
    count = 1
    
    for filename in files:
        old_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(old_path):
            if extension and not filename.endswith(extension):
                continue
            
            file_ext = os.path.splitext(filename)[1]
            
            new_name = f"{prefix}_{count}{file_ext}"
            new_path = os.path.join(folder_path, new_name)
            
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")
            
            count += 1
