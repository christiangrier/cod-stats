from unittest import result
import easyocr 
import cv2
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import os

img_SS = 'img_SS'

def file_Creation():
    try:
        os.remove(img_SS)
    except OSError:
        pass
    
    if not os.path.exists(img_SS):
        os.makedirs(img_SS)
        # Make directory if not exists
        
    video = cv2.VideoCapture('')
        # Video to take screenshots of for processing   
    return 

def gen_Img(video):
    # Screen captures of the provided video based on a desired location and timing
    index = 0
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break

        name = '.image/frame' + str(index) + '.pdf'
            # This will be the naming convention for the screenshots
        if index % 30 == 0:
            print(name)
            cv2.imwrite(name, frame)
        index = index + 1
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()


def gen_Text():
    for i in os.listdir(img_SS):
        print(str(i))
        specific_SS = Image.open(img_SS + '/' + i)
        reader = easyocr.Reader(['en'])
        text = reader.readtext(img_SS)

#def gen_Text():
    # Image to text
    #IMAGE_PATH = 'images/double.png'
    #reader = easyocr.Reader(['en'])
    #result = reader.readtext(IMAGE_PATH)



if __name__ == "__main__":
    images = file_Creation()
    gen_Img(images)
    gen_Text()