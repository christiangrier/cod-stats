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

image = cv2.imread('./images/single.png')
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
img_Not = cv2.bitwise_not(grey)

cv2.imshow('Original', image)
cv2.imshow('Greyscale', grey)
cv2.imshow('Inverted', img_Not)

cv2.waitKey(0)
cv2.destroyAllWindows()
