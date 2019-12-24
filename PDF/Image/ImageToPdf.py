import os
from fpdf import FPDF

pdf = FPDF("L")

dirname = "C:/Users/D4R6/Documents/GOMPlayer/Capture"
imagelist = os.listdir(dirname)
for image in imagelist:
    full_filename = os.path.join(dirname, image)
    pdf.add_page()
    pdf.image(full_filename, 0, 0, 0, 170)

pdf.output("convert.pdf", "F")