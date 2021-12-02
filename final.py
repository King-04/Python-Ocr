import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image

#read image
img = cv2.imread('inv1.jpg') 

#preprocessing
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #grayscale

(thresh, bw) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY) #black and white

#display images
#cv2.imshow('Original image',img)
#cv2.imshow('Gray image', gray)
#cv2.imshow('Black white image', bw)

#cv2.waitKey(0)
#cv2.destroyAllWindows()



#Adding custom options

custom_config = r'--oem 3 --psm 6'
pytesseract.image_to_string(gray, config=custom_config)
