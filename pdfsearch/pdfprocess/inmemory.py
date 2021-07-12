from parser.pdfparser import PdfParser
from pdfprocess.tostorage import save_to_file
from tokenise.tokenise import Tokeniser

def in_memory_processing(parser: PdfParser, tokeniser: Tokeniser):
    dictionary_of_dictionaries_doc_based = {}
    dictionary_of_dictionaries_term_based = {}
    num_of_pages = parser.get_page_count()

    dictionary_of_dictionaries_doc_based = process_all_pages(num_of_pages, parser, tokeniser, dictionary_of_dictionaries_doc_based)

    dictionary_of_dictionaries_term_based = convert_to_term_based_dictionary(dictionary_of_dictionaries_doc_based)


    save_to_file(dictionary_of_dictionaries_doc_based)
    save_to_file(dictionary_of_dictionaries_term_based)

'''
doc_data: pair of (dictionary of data in doc, num of terms in doc)

'''
def process_all_pages(num_of_pages: int, parser: PdfParser, tokeniser: Tokeniser, dictionary_of_dictionaries_doc_based: dict):
    for pg_number in range(0, num_of_pages):
        doc_data = parse_page(pg_number, parser, tokeniser)
        dictionary_of_dictionaries_doc_based[pg_number] = doc_data
    return dictionary_of_dictionaries_doc_based

def parse_page(pg_number: int, parser: PdfParser, tokeniser: Tokeniser):
    doc = parser.get_doc(pg_number)
    num_of_terms_in_page = tokeniser.get_num_terms_in_page(doc)
    dictionary_of_page = tokeniser.tokenise_doc(doc) 
    return (dictionary_of_page, num_of_terms_in_page)

# TODO: (urgent)
def convert_to_term_based_dictionary(dictionary_of_dictionaries_doc_based: dict):
    ...
