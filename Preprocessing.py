import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image

#read image
img = cv2.imread(image) #image to read from

#preprocessing

#grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #grayscale

#black and white
(thresh, bw) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
