import easyocr
from mss import mss 
from PIL import Image, ImageGrab
from PIL import *
import pytesseract
import pandas as pd
import os
from natsort import natsorted
import cv2

image = "test_Image"

# IMAGE_PATH = 'Image/frame1800.png'
# reader = easyocr.Reader(['en'])
# result = reader.readtext(IMAGE_PATH)

# print(result)

def get_Text():
    appended_Data = []
    for i in natsorted(os.listdir(image)):
        #print(str(i))
        my_example = Image.open(image + '/' + i)
        x, y, w, h = 29, 426, 186, 19
        ROI = my_example.crop((x, y, x + w, y + h))
        text = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
        #print(text)
        appended_Data.append(text)
        #df = pd.DataFrame({'Text': [text]})
        #print(df)
        #print(appended_Data)
    
    df = pd.DataFrame(appended_Data)
    print(df)

if __name__ == '__main__':
    get_Text()