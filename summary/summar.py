import nltk
from nltk.corpus import stopwords
import itertools
from text_preprocess.text_pre import text_processing
import re
from gensim import corpora, models
from operator import itemgetter
class Text_summary():
    def __init__(self,text):
        self.text = text

    def clean_text(self):
        text = re.sub(r'\[[0-9]*\]', ' ', self.text)
        text = re.sub(r'\s+', ' ', self.text)
        text = re.sub('[^a-zA-Z]', ' ', self.text )
        text = re.sub(r'\s+', ' ', self.text)
        
        return text

    def sent_toke(self,text):
        sent_to = nltk.sent_tokenize(text)
        return sent_to

    def word_frq(self,clean_texts):
        stopwords = nltk.corpus.stopwords.words('english')
        word_freq = {}
        for word in nltk.word_tokenize(clean_texts):
            if word not in stopwords:
                if word not in word_freq.keys():
                    word_freq[word] = 1
                else:
                    word_freq[word] +=1

        return word_freq

    def sent_score(self,words_frq):
        sent_scores={}
        sent = nltk.sent_tokenize(self.text)

        for sent in sent:
            for word, freq in words_frq.items():
                if word in sent.lower():
                    if sent in sent_scores:
                        sent_scores[sent] += freq
                    else:
                        sent_scores[sent] = freq
        return sent_scores


    def genrate_summary(self):

        clean_text = self.clean_text()
        words_frq = self.word_frq(clean_texts=clean_text)
        sent_score = self.sent_score(words_frq)

        sumvalues = 0
        for sent in sent_score:
            sumvalues += sent_score[sent]
        average = int(sumvalues / len(sent_score))

        summary = ''
        for sent in nltk.sent_tokenize(self.text):
            if (sent in sent_score) and (sent_score[sent] > (average)):
                summary += " " + sent
        return summary

   