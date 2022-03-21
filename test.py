import easyocr
from mss import mss 
from PIL import Image, ImageGrab
from PIL import *
import pytesseract
import os
from natsort import natsorted
import cv2

image = "Image"

# IMAGE_PATH = 'Image/frame1800.png'
# reader = easyocr.Reader(['en'])
# result = reader.readtext(IMAGE_PATH)

# print(result)

def get_Text():
    for i in natsorted(os.listdir(image)):
        print(str(i))
        my_example = Image.open(image + '/' + i)
        #x, y, w, h = 55, 934, 395, 36
        #ROI = my_example.crop((x, y, x + w, y + h))
        x, y, w, h = 29, 426, 186, 19
        ROI = my_example.crop((x, y, x + w, y + h))
        text = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
        #text.show()
        print(text)


if __name__ == '__main__':
    get_Text()