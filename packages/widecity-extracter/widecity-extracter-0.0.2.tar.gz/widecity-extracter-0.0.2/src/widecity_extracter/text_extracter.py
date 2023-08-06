import os
from PIL import Image
from pytesseract import pytesseract
import shutil
# Defining paths to tesseract.exe
# and the image we would be using
path_to_tesseract = r"teract\tesseract.exe"

def extract_text(image,requirement):
    image_path = image
    img = Image.open(image_path)
    try:
        pytesseract.tesseract_cmd = path_to_tesseract
    except:
        return 'pytesseract not found'
    text = pytesseract.image_to_string(img)
    text = str(text).capitalize()
    try:
        if text.index(requirement):
            return True
    except:
        return False


def getmybills(folder_path,requirement):
    result= []
    for image in os.listdir(folder_path):
        found = extract_text(folder_path+'/'+image,requirement)
        if found == 'pytesseract not found':
            return 'pytesseract not found'
        elif found:
            result.append(image)
            shutil.copy(folder_path+'/'+image,'results')
    return result


print(getmybills('bills','total'))