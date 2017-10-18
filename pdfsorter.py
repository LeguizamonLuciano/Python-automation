#! python3
import PyPDF2, os

pdfFiles = []
for filename in os.listdir('.'): #se le pasa un directorio o actua donde este guardado el programa
    if filename.endswith('.pdf'):#si terminan los archivos leidos con .pdf
        pdfFiles.append(filename)#almacena dichos archivos en pdfFiles
pdfWriter = PyPDF2.PdfFileWriter()
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
for pageNum in range(0,pdfReader.numPages,2):#0 hasta cantidad de paginas de 2 en 2 (0,2,4,n...)
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)#devuelve el pdf rearmado
pdfOutput.close()
