import PyPDF2

def extrator_pdf(filename):
    pdfFile = open(filename,'rb')

    pdfreader = PyPDF2.PdfFileReader(pdfFile)

    pageobj = pdfreader.getPage(0)

    text = pageobj.extract_text()