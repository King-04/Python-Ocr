#creating textfile from output
output = pytesseract.image_to_string(gray, config=custom_config)
with open('readme.txt', 'w') as f:
    f.writelines(output)
