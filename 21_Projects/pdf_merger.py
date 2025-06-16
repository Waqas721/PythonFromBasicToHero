# https://pypdf2.readthedocs.io/en/3.x/user/merging-pdfs.html

from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs=[]
n=int(input("how many pdf you want to merge?\n "))
for i in range(0,n):
    name=input(f"Enter the name of the PDF  {i+1}:")
    pdfs.append(name)
    
for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()