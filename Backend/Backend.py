from flask import Flask, request, jsonify, send_file, make_response
from flask_cors import CORS
import os
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from PyPDF2 import PdfReader, PdfReader, PdfWriter

#will change to a folder located in the server
UPLOAD_FOLDER = '/home/yranda/Documents/Deep_dive/Resources/uploadFolder'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


CORS(app) # Enable CORS on server side

text="Watermarkflasktest"
out_path='/home/yranda/Documents/Deep_dive/prueba/Watermarked.pdf'



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

@app.route('/submit-form', methods=['POST'])
def submit_form():
    email = request.form['email']
    date = request.form['currentDate']
    file = request.files['file']
    filename=file.filename   
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    makeWatermark(text)
    file_path=os.path.join(app.config['UPLOAD_FOLDER'], filename)
    makepdf(file_path)

    print(f"Received email {email} at {date} with namefile {filename} {text}")
    return {'message': 'File uploaded successfully!, text {text}'}
    




if __name__ == '__main__':
    from waitress import serve
    # This line is to debug requests made to the server on development
    app.run(use_reloader=True, port=3001, threaded=True)
    # This is to run the server on deployment and get full performance
    #serve(app, host="0.0.0.0", port=3000, url_scheme='https')