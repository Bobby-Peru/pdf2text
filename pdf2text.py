import PyPDF2
import os

pdf_path = '/pdf/path/'

files = os.listdir(pdf_path)

for book in files:
    if book != '.DS_Store' and os.path.isfile(pdf_path + book):
        text = ""
        with open(pdf_path + book, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
    
        with open(pdf_path + 'output/' + book[:-3] + 'txt', 'w') as f:
            f.write(text)
