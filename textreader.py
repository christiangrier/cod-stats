from PIL import Image
from matplotlib import image
import pytesseract
import pyautogui
import os
import cv2
import numpy as np


image = 'Image'

def files_Creation():
    try:
        os.remove(image)
    except OSError:
        pass
    
    if not os.path.exists(image):
        os.makedirs(image)
        # Make directory if not exists
        
    src_vid = cv2.VideoCapture('Winners_Finals_OpticVRavens.mp4')
        # Video to take screenshots of for processing   
    return(src_vid)

x = 55
y = 934
h = 36
w = 395

def gen_Img(src_vid):
    index = 0
    if not src_vid.isOpened():
        print("could not open src_vid")
        exit()
    
    while (1):
        ret, frame = src_vid.read()
        
        if not ret:
            break

        name = './image/frame' + str(index) + '.png'
            # This will be the naming convention for the screenshots
        if index % 1800 == 0:
            print("capturing..." + name)
            #crop = frame[y:y+h, x:x+w]
            cv2.imwrite(name, frame)
        index = index + 1
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        
    src_vid.release()
    cv2.destroyAllWindows()
    
def get_Text():
    for i in os.listdir(image):
        print(str(i))
        my_example = Image.open(image + '/' + i)
        text = pytesseract.image_to_string(my_example, lang='eng')
        print(text)
        
if __name__ == '__main__':
    vid = files_Creation()
    gen_Img(vid)
    get_Text()