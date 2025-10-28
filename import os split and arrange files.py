import os
import shutil

# Step 1: Give your folder path
source_folder = r"C:\Users\admin"   

# Step 2: List of target folders for file types
file_types = {
    "PDF_Files": [".pdf"],
    "Excel_Files": [".xlsx", ".xls", ".csv"],
    "Word_Files": [".doc", ".docx"],
    "Images": [".jpg", ".jpeg", ".png"],
    "Text_Files": [".txt"],
    "PowerPoint": [".ppt", ".pptx"],
    "ZIP_Files": [".zip", ".rar"],
}


# Step 3: Create folders if not exist
for folder in file_types.keys():
    folder_path = os.path.join(source_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Step 4: Move files into folders
for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)
    if os.path.isfile(file_path):
        for folder, extensions in file_types.items():
            if any(file.lower().endswith(ext) for ext in extensions):
                dest_path = os.path.join(source_folder, folder, file)
                shutil.move(file_path, dest_path)
                print(f"Moved: {file} → {folder}")
                break
