import docx

def read_docx_text(path):
    doc = docx.Document(path)
    text = ''
    for para in doc.paragraphs:
        text += para.text + '\n'
    return text
