import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
from PIL import Image,__version__
import pandas as pd
import csv
image = Image.open("Assi.png")
text = tess.image_to_string(image)
# print(text)
# Split the extracted text into lines
lines = text.split("\n")
csv_file = 'data.csv'
encodings = ['utf-8']
# Open the CSV file with the correct encoding

with open(csv_file, 'a', newline='',) as file:
    writer = csv.writer(file)
    for string in lines:
        writer.writerow([string])
