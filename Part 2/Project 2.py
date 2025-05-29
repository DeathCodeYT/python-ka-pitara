# Folder Organizer with Logging
import os
import shutil

folder_path = r"C:\Users\DeathCode\Desktop\RandomFiles"

extension_map = {
    "Images":['.jpg','.bmp','.png','.gif','.jpeg'],
    "Videos":['.mp4','.mkv','.mov','.avi'],
    "Documents":['.pdf','.doc','.docx','.txt','.pptx','xlsx'],
    "Music":['.mp3', '.wav', '.flac','.aac'],
    "Archives":['.zip', '.rar', '.7z', '.tar.gz'],
    "Scripts":['.py', '.js', '.bat', '.ps1', '.sh', '.html'],
    "Programs":['.exe','.msi','.deb','.dmg','.pkg'],
    "Others":[],
}

from datetime import datetime

log_file = os.path.join(folder_path,"organizer_log.txt")
with open(log_file,'a') as log:
    log.write(f"\n----- Organizing started at {datetime.now()} -----\n")

for file in os.listdir(folder_path):
    full_path = os.path.join(folder_path,file)

    if file == 'organizer_log.txt':
        continue

    if os.path.isfile(full_path):
        ext = os.path.splitext(file)[-1].lower()
        moved = False
    
        for folder,extensions in extension_map.items():
            if ext in extensions:
                target_dir = os.path.join(folder_path,folder)
                os.makedirs(target_dir,exist_ok=True)
                shutil.move(full_path,target_dir)
                with open(log_file,'a') as log:
                    log.write(f"Moved: {file} -> {folder}\n")
                moved = True
                break
        if not moved:
            target_dir = os.path.join(folder_path,"Others")
            os.makedirs(target_dir,exist_ok=True)
            shutil.move(full_path,target_dir)
            with open(log_file,'a') as log:
                    log.write(f"Moved: {file} -> {folder}\n")

print("✅ Files organized successfully! Log saved in organizer_log.txt")


