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

start = (55, 970)
end = (450, 934)
color = (0, 255, 0)
thickness = 1

def gen_Img(src_vid):
    index = 0
    if not src_vid.isOpened():
        print("could not open src_vid")
        exit()
    
    while (1):
        ret, frame = src_vid.read()
        display = cv2.rectangle(frame.copy(), start, end, color, thickness)
        ROI = frame[934:970, 55:450].copy()
        
        if not ret:
            break

        name = './image/frame' + str(index) + '.png'
            # This will be the naming convention for the screenshots
        if index % 400 == 0:
            print("capturing..." + name)
            cv2.imwrite(name, ROI)
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