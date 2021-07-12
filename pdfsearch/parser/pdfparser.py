import PyPDF2
import time
import nltk


class PdfParser:
    def __init__(self, pdf_path: str):
        self.pdfReader = PyPDF2.PdfFileReader(open(pdf_path, 'rb'))


    def get_page_count(self):
        return self.pdfReader.numPages

    def get_doc(self, page_number: int):
        pageObj = self.pdfReader.getPage(page_number)
        doc = pageObj.extractText()
        return doc