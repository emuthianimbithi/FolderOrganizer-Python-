import os
import shutil

def organize_files(directory):
    files = os.listdir(directory)
    
    for file in files:
        file_path = os.path.join(directory, file)
        
        if os.path.isfile(file_path):
            _, file_ext = os.path.splitext(file)
            if not os.path.exists(os.path.join(directory, file_ext[1:])):
                os.makedirs(os.path.join(directory, file_ext[1:]))
            
            shutil.move(file_path, os.path.join(directory, file_ext[1:], file))
directory_to_organize = 'D:\\New folder'
organize_files(directory_to_organize)
