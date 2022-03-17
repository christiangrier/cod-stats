from unittest import result
import easyocr 
import cv2
from matplotlib import pyplot as plt
import numpy as np

def gen_Img(video):
    # Screen captures of the provided video based on a desired location and timing
    index = 0
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break





def gen_Text():
    # Image to text
    IMAGE_PATH = 'images/double.png'
    reader = easyocr.Reader(['en'])
    result = reader.readtext(IMAGE_PATH)

    print(result)


if __name__ == "__main__":
    gen_Img()
    # need to pass something here^, havent made that yet
    gen_Text()