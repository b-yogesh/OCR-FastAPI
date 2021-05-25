import pytesseract
from pytesseract import Output
import os
import cv2
pytesseract.pytesseract.tesseract_cmd = f'C:/Program Files/Tesseract-OCR/tesseract'

def extract(img_path):
    try:
        data =  pytesseract.image_to_data(img_path, output_type=Output.DICT)
        image = get_bboxes(data, img_path)
        save_path = 'ocr-app/static/temp'
        cv2.imwrite(os.path.join(save_path, 'overlayed_image.png'), image)
        return True
    except:
        return False

def get_bboxes(data, img_path):
    img = cv2.imread(img_path)
    n_boxes = len(data['level'])
    for i in range(n_boxes):
        (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return img