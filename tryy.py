import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image
from pdf2image import convert_from_path

import re
import requests


#convert pdf to images
pdfs = r"ernest.pdf"
pages = convert_from_path(pdfs, 300)

for page in pages:
    page.save('pic.jpg', 'JPEG')



#read image
img = cv2.imread('pic.jpg') 

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
text = pytesseract.image_to_string(bw,config=custom_config)

print(text)



-------------------------------------------------------------------------------------------
for row in text.split('\n'):
    if row.startswith('SUB TOTAL'):
        subtot = row.split()[-1]
        
for row in text.split('\n'):
    if row.startswith('DISCOUNT'):
        dis = row.split()[-1]
        
#for row in text.split('\n'):
#    if row.startswith('TAX'):
#        tax = row.split()[-1]
        
for row in text.split('\n'):
    if row.startswith('INVOICE TOTAL'):
        invtot = row.split()[-1]
        
print("SUB TOTAL = " +subtot)
print("DISCOUNT = " +dis)
#print("TAX = " +tax)
print("INVOICE TOTAL = " +invtot)





---------------------------------------------------------------------------------------------
inv_line_re = re.compile(r'^(\w+( \w+)*) ([\d]+\.\d{2})')

for line in text.split('\n'):
    if inv_line_re.search(line):
        output = line
        #print(line)
        
#inv_head_re = re.compile(r'^(\w+( \w+)*) (?:[A-Z]+ ){2}[A-Z]+')

#for head in text.split('\n'):
#    if inv_head_re.search(head):
#        heading = head
#        print(head)

def convert(inp):
    return (inp.split())

#put output into a list
ldone = convert(output)
#hdone = convert(heading)
#print(ldone)
#print(hdone)

UNIT_PRICE = ldone[-3]
QUANTITY = ldone[-2]
AMOUNT = ldone[-1]

print("UNIT PRICE : "+ldone[-3])
print("QUANTITY : "+ldone[-2])
print("AMOUNT : "+ldone[-1])



