# Importing PdfWriter class from PyPDF2 library
from PyPDF2 import PdfWriter
# Importing os Module
import os

# Create a PdfWriter instance for merging PDFs
merger = PdfWriter()

# List all files in the current directory ending with ".pdf"
files = [file for file in os.listdir() if file.endswith(".pdf")]

# Iterate through each PDF file and append it to the merger
for pdf in files:
    merger.append(pdf)

# Write the merged PDF into a file named "merged.pdf"
merger.write("merged.pdf")

# Close the PdfWriter instance
merger.close()
