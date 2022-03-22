from PIL import Image
from matplotlib import image
from natsort import natsorted
from openpyxl.workbook import Workbook
import pytesseract
import pyautogui
import os
import cv2
import numpy as np
import pandas as pd 


image = 'Image'

def files_Creation():
    try:
        os.remove(image)
    except OSError:
        pass
    
    if not os.path.exists(image):
        # Make directory if not exists
        os.makedirs(image)
        
    # Video to take screenshots of for processing 
    src_vid = cv2.VideoCapture('Input video file name here')
          
    return(src_vid)

def gen_Img(src_vid):
    index = 0
    if not src_vid.isOpened():
        print("could not open src_vid")
        exit()
    
    while (1):
        ret, frame = src_vid.read()
        
        # if ret is read correctly ret is True
        if not ret:
            break
        
        # This will be the naming convention for the screenshots
        name = './image/frame' + str(index) + '.png'
        
        # Defining the framerate capture.
        # For my case, 3fps will do the job for capturing killfeed
        if index % 10 == 0:
            print("capturing..." + name)
            cv2.imwrite(name, frame)
        index = index + 1
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        
    src_vid.release()
    cv2.destroyAllWindows()
    
def get_Text():
    appended_Data = []
    for i in natsorted(os.listdir(image)):
        #print(str(i))
        my_example = Image.open(image + '/' + i)
        x, y, w, h = 29, 426, 186, 19
        ROI = my_example.crop((x, y, x + w, y + h))
        text = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
        #string to list for DataFrame preparations
        appended_Data.append(text)
        #print(appended_Data)
    
    #creating a dataframe for easy analysis with pandas
    df = pd.DataFrame(appended_Data)
    df.to_csv('Input csv name here')
    #print(df)
        
if __name__ == '__main__':
    vid = files_Creation()
    gen_Img(vid)
    get_Text()