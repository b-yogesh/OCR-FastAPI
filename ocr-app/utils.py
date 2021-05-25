import os
import shutil

# Saves uploaded files to disk for processing
def save_temp_file(file, path):
    file_name = 'ocr-app/static/temp'
    extension = os.path.splitext(file.filename)[-1]
    temp_file = os.path.join(file_name, 'temp'+extension)
    with open(temp_file, 'wb') as f:
        shutil.copyfileobj(file.file, f)
    return temp_file