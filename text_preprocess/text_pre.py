from review_sentiment.review import Preprocess_review
import pandas as pd
import numpy as np

class text_processing(Preprocess_review):
    def __init__(self):
        super().__init__()
        
    def text_preprocese(self,corpus,remove_punctuation=True,remove_html_tag=True,remove_url=True, remove_emoji=True,
    remove_abb=True,remove_special_characters=True,remove_whitespace=True,remove_stopwords=True,
    stem_words=True,text_lower_case=True):
        normized_corpus = []
        for doc in corpus:
            if remove_punctuation:
                doc = self.remove_punctuations(doc)
            if remove_html_tag:
                doc = self.remove_html_tag(doc)
            if remove_url:
                doc = self.remove_url(doc)
            if remove_emoji:
                doc = self.remove_emoji(doc)
            if remove_abb:
                doc = self.remove_abb(doc)
            if remove_special_characters:
                doc = self.remove_special_characters(doc)
            if remove_whitespace:
                doc = self.remove_whitespace(doc)
            if remove_stopwords:
                doc = self.remove_stopwords(doc)
            if stem_words:
                doc = self.stem_words(doc)
            
            normized_corpus.append(doc)
        return normized_corpus