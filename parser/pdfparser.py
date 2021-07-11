import PyPDF2
import time
import nltk

file_name = "parser/test.pdf"

class PdfParser:
    def __init__(self, pdf_path: str):
        self.pdfReader = PyPDF2.PdfFileReader(open(file_name, 'rb'))


    def get_page_count(self):
        return self.pdfReader.numPages

    def get_page(self, page_number: int):
        pageObj = self.pdfReader.getPage(page_number)
        return pageObj.extractText()
