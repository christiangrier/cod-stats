import easyocr
from mss import mss 
from PIL import Image, ImageGrab

IMAGE_PATH = 'images/optic.png'
reader = easyocr.Reader(['en'])
result = reader.readtext(IMAGE_PATH)

print(result)
