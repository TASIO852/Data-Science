import pandas as pd  # Unificar planilhas
import PyPDF2 as pdf

def convert_pdf(pdfload):

    pdffile = open(pdfload, 'rb')

    pdfreader = pdf.PdfFileReader(pdffile)

    pageobj = pdfreader.getPage(0)

    text = pageobj.extract_text()

    rows = []
    rows.append(text.strip())
    df = pd.DataFrame(rows)
    df.to_csv('C:/Users/tasio.guimaraes/Documents/Export my project/src/myfile.csv')
