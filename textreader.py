from unittest import result
import easyocr 
import cv2
from matplotlib import pyplot as plt
import numpy as np

IMAGE_PATH = 'images/double.png'
reader = easyocr.Reader(['en'])
result = reader.readtext(IMAGE_PATH)

print(result)
