import pytesseract
import os

def extract(img_path, lang='eng'):
    try:
        return pytesseract.image_to_string(img_path, lang=lang)
    except:
        return f"Unable to process file: {img_path}"