import PyPDF2

with open('archivo_original.pdf', 'rb') as archivo_original:
    pdf_reader = PyPDF2.PdfFileReader(archivo_original)


    pdf_writer = PyPDF2.PdfFileWriter()

    for pagina in range(pdf_reader.getNumPages()):
        pagina_actual = pdf_reader.getPage(pagina)
        marca_de_agua = PyPDF2.PdfFileReader(open('marca_de_agua.pdf', 'rb')).getPage(0)
        pagina_actual.mergePage(marca_de_agua)
        pdf_writer.addPage(pagina_actual)

    with open('archivo_con_marca_de_agua.pdf', 'wb') as archivo_con_marca_de_agua:
        pdf_writer.write(archivo_con_marca_de_agua)