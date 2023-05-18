from flask import Flask, request, jsonify, send_file, make_response
from flask_cors import CORS
import os
import sys
import csv
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from PyPDF2 import PdfReader, PdfReader, PdfWriter
from flask_mail import Mail, Message
from emailsends import send_email
from datetime import datetime, timedelta
from makes_csv import create_csv
from emailsends import send_Admin
import schedule
import time

from timeloop import Timeloop


#will change to a folder located in the server
UPLOAD_FOLDER = 'Backend/uploadfolder'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CORS(app) # Enable CORS on server side
csv_path="prueba/resumen.csv"
out_path='prueba/Watermarked.pdf'
tl=Timeloop()
def makepdf(pdf_file):
    watermark = 'watermark.pdf'
    merged = out_path


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



# Index route and most basic example
@app.route('/', methods=['GET'])
def index():
    return jsonify({"Status": "Online!"})

@tl.job(interval=timedelta(minutes=25))
def Admin():
    print("csv send")
    send_Admin()


@app.route('/submit-form', methods=['POST'])
def submit_form():
    email = request.form['email']
    date_time = datetime.now()
    date = date_time.strftime("%Y-%m-%d %H:%M:%S")
    file = request.files['file']
    logo=request.form['logo']
    time = datetime.now()
    filename=file.filename   
    file.save(os.path.join(UPLOAD_FOLDER, filename))
    makeWatermark(logo)
    file_path=os.path.join(UPLOAD_FOLDER, filename)
    makepdf(file_path)
    print(date)
    marked_pdf='prueba/Watermarked.pdf'
    print(f"Received email {email} at {date} with namefile {filename}  at {date}")
    send_email(email,marked_pdf)
    create_csv(csv_path,date,email)
    os.remove(file_path)
    return {'message': 'File uploaded successfully! '}
    




if __name__ == '__main__':
    from waitress import serve
    # This line is to debug requests made to the server on development
    tl.start()
    app.run(use_reloader=True, port=3001, threaded=True)
   
    # This is to run the server on deployment and get full performance
    #serve(app, host="0.0.0.0", port=3000, url_scheme='https')