import fitz  # PyMuPDF

def read_pdf_text(path):
    text = ''
    doc = fitz.open(path)
    for page in doc:
        text += page.get_text()
    return text
