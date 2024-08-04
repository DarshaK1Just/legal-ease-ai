import PyPDF2
import docx

def read_pdf(file):
    pdf_reader = PyPDF2.PdfFileReader(file)
    text = ""
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text += page.extract_text()
    return text

def read_docx(file):
    doc = docx.Document(file)
    text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
    return text

def read_txt(file):
    return file.read().decode("utf-8")

def read_file(file):
    if file.type == "application/pdf":
        return read_pdf(file)
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return read_docx(file)
    elif file.type == "text/plain":
        return read_txt(file)
    else:
        raise ValueError("Unsupported file type")
