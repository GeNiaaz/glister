from parser.pdfparser import PdfParser
from pdfprocess.inmemory import in_memory_processing
from tokenise.tokenise import Tokeniser


# TODO: change this to be passed in, instead of hardcoded
is_punct = is_case_fold = is_stem = True

'''
input: takes in path to pdf
saves data to storage

'''
# TODO: add flag to indicate type of processing, now simply in memory for simplicity
def process_pdf(filename: str):
    parser = PdfParser(filename)
    tokeniser = Tokeniser(is_punct, is_case_fold, is_stem)

    in_memory_processing(parser, tokeniser)
