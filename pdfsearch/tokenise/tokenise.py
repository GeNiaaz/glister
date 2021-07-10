import sys

from etc.constants import PUNCTUATION
import nltk
from nltk.stem import PorterStemmer


class Tokenise: 
    def __init__(self, is_punct: bool, ):
        self.stemmer = PorterStemmer;
        self.doc_dictionary_of_terms = {}
        self.is_punctuation = is_punct

    ''' Primary called function '''
    def tokenise_doc(self, doc):
        sentences = self.tokenise_to_sentences(doc)
        self.process_sentences(sentences)

        return self.dictionary_of_terms

    ''' Secondary called functions '''
    def process_sentences(self, sentences):
        for sentence in sentences:
            terms = self.process_each_sentence(sentence)
            self.process_terms(terms)

    def tokenise_to_sentences(doc):
        return nltk.sent_tokenize(doc)

    def process_terms(self, terms):
        for term in terms:
            # Processing term
            if self.is_punctuation:
                term = self.punctation_processing(term)
            if self.is_case_fold:
                term = self.case_fold_term(term)
            if self.is_stem:
                term = self.stem_term(term)
            
            # Saving term to memory
            self.save_to_mem(term)

    def save_to_mem(self, term):
        if term not in self.doc_dictionary_of_terms:
            self.doc_dictionary_of_terms[term] = 1
        else:
            current_freq = self.dictionary_of_terms[term]
            self.doc_dictionary_of_terms[term] = current_freq + 1

    def tokenise_to_terms(sentence):
        return nltk.word_tokenize(sentence)
        

    def punctuation_processing(term):
        if term in PUNCTUATION:
            term = ""
        else: 
            for p in PUNCTUATION:
                term.replace(p, "")
        return term

    def case_fold_term(term):
        return term.lower()

    def stem_term(self, term):
        return self.stemmer.stem(term)
