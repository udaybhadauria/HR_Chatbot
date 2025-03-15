import fitz  # PyMuPDF

def extract_text_from_pdf(file_path):
    """Load a PDF and extract text."""
    doc = fitz.open(file_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text
