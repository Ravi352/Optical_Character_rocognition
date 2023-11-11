import fitz  # PyMuPDF

# Replace 'your_pdf.pdf' with the path to your PDF file
pdf_file = 'Assign.pdf'

# Replace page_number with the page number you want to rotate (e.g., 0 for the first page)
page_number = 0

# Open the PDF file
pdf_document = fitz.open(pdf_file)

# Get the specified page
page = pdf_document[page_number]

# Rotate the page 90 degrees clockwise
page.setRotation(90)

# Save the modified PDF to a new file
# Replace 'output_rotated.pdf' with the desired output file name
output_file = 'output_rotated.pdf'
pdf_document.save(output_file)

# Close the PDF document
pdf_document.close()