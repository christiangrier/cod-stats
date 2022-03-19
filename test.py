import easyocr
from mss import mss 
from PIL import Image, ImageGrab
import pytesseract
import os

image = "Image"

#IMAGE_PATH = 'images/optic.png'
#reader = easyocr.Reader(['en'])
#result = reader.readtext(IMAGE_PATH)

#print(result)

def get_Text():
    for i in os.listdir(image):
        print(str(i))
        #my_example = Image.open(image + '/' + i)
        IMAGE_PATH = image + '/' + i
        reader = easyocr.Reader(['en'])
        text = reader.readtext(IMAGE_PATH, detail=0)
        
        #text = pytesseract.image_to_string(my_example, lang='eng')
        print(text)


if __name__ == '__main__':
    get_Text()