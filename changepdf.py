
from PyPDF2 import PdfReader, PdfReader, PdfWriter

input_pdf='/home/yranda/Documents/Deep_dive/Lorem.pdf'
#output='/home/yranda/Documents/Deep_dive/Resources'
#watermark='Resources/watermark.png'
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
import smtplib, ssl


#text = input("Enter the watermark text here:")
text="Hola noo"
pdf_file='/home/yranda/Documents/Deep_dive/Lorem.pdf'

def makepdf(pdf_file):
    watermark = 'watermark.pdf'
    merged = "Watermarked.pdf"

    with open(pdf_file, "rb") as input_file, open(watermark, "rb") as watermark_file:
        input_pdf = PdfReader(input_file)
        watermark_pdf = PdfReader(watermark_file)
        watermark_page = watermark_pdf.pages[0]
        output = PdfWriter()

        for i in range(len(input_pdf.pages)):
            pdf_page = input_pdf.pages[i]
            pdf_page.merge_page(watermark_page)

            output.add_page(pdf_page)

        with open(merged, "wb") as merged_file:
            output.write(merged_file)




def makeWatermark(text):   
    pdf = canvas.Canvas("watermark.pdf", pagesize=A4)
    pdf.translate(inch, inch)
    pdf.setFillColor(colors.grey, alpha=0.6)
    pdf.setFont("Helvetica", 50)
    pdf.rotate(45)
    pdf.drawCentredString(400, 100, text)
    pdf.save()






makeWatermark(text)
#aprender como subir un archivo
makepdf(pdf_file)