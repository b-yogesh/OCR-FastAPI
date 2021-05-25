import os
import shutil
import glob

# Saves uploaded files to disk for processing
def save_temp_file(file, path):
    file_name = 'ocr-app/static/temp'
    extension = os.path.splitext(file.filename)[-1]
    temp_file = os.path.join(file_name, 'temp'+extension)
    with open(temp_file, 'wb') as f:
        shutil.copyfileobj(file.file, f)
    return temp_file

def remove_temp_files(folder, path):
    shutil.rmtree(os.path.join(folder, path))
    access_rights = 0o777
    os.mkdir(path, access_rights)