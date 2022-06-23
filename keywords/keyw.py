import nltk
from nltk.corpus import stopwords
import itertools

from sqlalchemy import false
from text_preprocess.text_pre import text_processing
import re
from gensim import corpora, models
from operator import itemgetter
from review_sentiment.review import Preprocess_review
from gensim.models import TfidfModel

class Get_keywords(text_processing):
    def __init__(self,text):
        super().__init__()
        self.text = text

    def clean(self):

        sent_to = nltk.sent_tokenize(self.text)
     
        return sent_to

    def test_clean(self,sents):
        text = self.text_preprocese(sents,text_lower_case=false,remove_stopwords=False,stem_words=False)
        return text


    def get_chunk(self,sent,grammar = r'NP: {<DT>? <JJ>* <NN.*>+}'):
        stopwords = nltk.corpus.stopwords.words('english')
        all_chunks = []
        chunker = nltk.chunk.regexp.RegexpParser(grammar)
      
        for s in sent:
            tagged_sents = [nltk.pos_tag(nltk.word_tokenize(s))]
            
            chunks =[chunker.parse(tagges_sent) for tagges_sent in tagged_sents]
            
            wtc_sents = [nltk.chunk.tree2conlltags(chunk) for chunk in chunks]
            flattened_chunks = list(
                            itertools.chain.from_iterable(
                                wtc_sent for wtc_sent in wtc_sents)
                           )
            
            valid_chunks_tagged = [(status, [wtc for wtc in chunk]) 
                                    for status, chunk 
                                        in itertools.groupby(flattened_chunks, 
                                                    lambda word_pos_chunk: word_pos_chunk[2] != 'O')]
            
            valid_chunks = [' '.join(word.lower() 
                                    for word, tag, chunk in wtc_group 
                                        if word.lower() not in stopwords) 
                                            for status, wtc_group in valid_chunks_tagged
                                                if status]
                                            
            all_chunks.append(valid_chunks)
       
        return all_chunks

    def get_tfidf_weighted_keyphrases(self,sentences, grammar=r'NP: {<DT>? <JJ>* <NN.*>+}',top_n=10):
    

        valid_chunks = self.get_chunk(sentences, grammar=grammar)                             
        dictionary = corpora.Dictionary(valid_chunks)
        corpus = [dictionary.doc2bow(chunk) for chunk in valid_chunks]
       
        tfidfs =TfidfModel(corpus,dictionary)
        corpus_tfidf = tfidfs[corpus]
        
      
        
        weighted_phrases = {dictionary.get(idx): value 
                            for doc in corpus_tfidf 
                                for idx, value in doc}
             
        weighted_phrases = sorted(weighted_phrases.items(), 
                                key=itemgetter(1), reverse=True)
        weighted_phrases = [(term, round(wt, 3)) for term, wt in weighted_phrases]
        
      
        return weighted_phrases[:top_n]

    def get_keywords(self):
        all_keywords = []
        text = self.clean()
        clean_text = self.test_clean(text)
        chunnks = self.get_chunk(clean_text)
        get_tf = self.get_tfidf_weighted_keyphrases(clean_text)
        for i,k in enumerate(get_tf):
            all_keywords.append(k[0])
        return all_keywords
       

       