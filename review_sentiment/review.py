import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
class Preprocess_review:
    def __init__(self):
        pass

    def display(self,data):
        df = pd.read_csv(data)
        return df

    def null_present(self,data):
        data = self.display(data)
        self.null_present = False
        try:
            self.null_count = data.isnull().sum()
            for i in self.null_count:
                if i > 0:
                    self.null_present = True
                    break
            return self.null_present
        except Exception as e:
            raise(e)

    def spilt_data(self,data):
        df= self.display(data)
        
        self.new_df = df.iloc[:40000,:]
        self.test_df = df.iloc[4000:,:]
        self.new_df.to_csv('test/test.csv')
        return self.new_df

    def remove_punctuations(self,data):
        try:
            self.data = re.sub(r'[^\w\s]', '', str(data))
            return self.data
        except Exception as e:
            raise(e)
    def remove_html_tag(self,data):
        html_tag = re.compile(r'<.*?>')
        data = html_tag.sub(r' ',data)
        return data

    def remove_url(self,data):
        url_clean= re.compile(r"https://\S+|www\.\S+")
        data=url_clean.sub(r' ',data)
        return data

    def remove_emoji(self,data):
        emoji_clean= re.compile("["
                            u"\U0001F600-\U0001F64F"  # emoticons
                            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                            u"\U0001F680-\U0001F6FF"  # transport & map symbols
                            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            u"\U00002702-\U000027B0"
                            u"\U000024C2-\U0001F251"
                            "]+", flags=re.UNICODE)
        data=emoji_clean.sub(r'',data)
        url_clean= re.compile(r"https://\S+|www\.\S+")
        data=url_clean.sub(r' ',data)
        return data

    def remove_abb(self,data):
        data = re.sub(r"he's", "he is", data)
        data = re.sub(r"there's", "there is", data)
        data = re.sub(r"We're", "We are", data)
        data = re.sub(r"That's", "That is", data)
        data = re.sub(r"won't", "will not", data)
        data = re.sub(r"they're", "they are", data)
        data = re.sub(r"Can't", "Cannot", data)
        data = re.sub(r"wasn't", "was not", data)
        data = re.sub(r"don\x89Ûªt", "do not", data)
        data= re.sub(r"aren't", "are not", data)
        data = re.sub(r"isn't", "is not", data)
        data = re.sub(r"What's", "What is", data)
        data = re.sub(r"haven't", "have not", data)
        data = re.sub(r"hasn't", "has not", data)
        data = re.sub(r"There's", "There is", data)
        data = re.sub(r"He's", "He is", data)
        data = re.sub(r"It's", "It is", data)
        data = re.sub(r"You're", "You are", data)
        data = re.sub(r"I'M", "I am", data)
        data = re.sub(r"shouldn't", "should not", data)
        data = re.sub(r"wouldn't", "would not", data)
        data = re.sub(r"i'm", "I am", data)
        data = re.sub(r"I\x89Ûªm", "I am", data)
        data = re.sub(r"I'm", "I am", data)
        data = re.sub(r"Isn't", "is not", data)
        data = re.sub(r"Here's", "Here is", data)
        data = re.sub(r"you've", "you have", data)
        data = re.sub(r"you\x89Ûªve", "you have", data)
        data = re.sub(r"we're", "we are", data)
        data = re.sub(r"what's", "what is", data)
        data = re.sub(r"couldn't", "could not", data)
        data = re.sub(r"we've", "we have", data)
        data = re.sub(r"it\x89Ûªs", "it is", data)
        data = re.sub(r"doesn\x89Ûªt", "does not", data)
        data = re.sub(r"It\x89Ûªs", "It is", data)
        data = re.sub(r"Here\x89Ûªs", "Here is", data)
        data = re.sub(r"who's", "who is", data)
        data = re.sub(r"I\x89Ûªve", "I have", data)
        data = re.sub(r"y'all", "you all", data)
        data = re.sub(r"can\x89Ûªt", "cannot", data)
        data = re.sub(r"would've", "would have", data)
        data = re.sub(r"it'll", "it will", data)
        data = re.sub(r"we'll", "we will", data)
        data = re.sub(r"wouldn\x89Ûªt", "would not", data)
        data = re.sub(r"We've", "We have", data)
        data = re.sub(r"he'll", "he will", data)
        data = re.sub(r"Y'all", "You all", data)
        data = re.sub(r"Weren't", "Were not", data)
        data = re.sub(r"Didn't", "Did not", data)
        data = re.sub(r"they'll", "they will", data)
        data = re.sub(r"they'd", "they would", data)
        data = re.sub(r"DON'T", "DO NOT", data)
        data = re.sub(r"That\x89Ûªs", "That is", data)
        data = re.sub(r"they've", "they have", data)
        data = re.sub(r"i'd", "I would", data)
        data = re.sub(r"should've", "should have", data)
        data = re.sub(r"You\x89Ûªre", "You are", data)
        data = re.sub(r"where's", "where is", data)
        data = re.sub(r"Don\x89Ûªt", "Do not", data)
        data = re.sub(r"we'd", "we would", data)
        data = re.sub(r"i'll", "I will", data)
        data = re.sub(r"weren't", "were not", data)
        data = re.sub(r"They're", "They are", data)
        data = re.sub(r"Can\x89Ûªt", "Cannot", data)
        data = re.sub(r"you\x89Ûªll", "you will", data)
        data = re.sub(r"I\x89Ûªd", "I would", data)
        data = re.sub(r"let's", "let us", data)
        data = re.sub(r"it's", "it is", data)
        data = re.sub(r"can't", "cannot", data)
        data = re.sub(r"don't", "do not", data)
        data = re.sub(r"you're", "you are", data)
        data = re.sub(r"i've", "I have", data)
        data = re.sub(r"that's", "that is", data)
        data = re.sub(r"i'll", "I will", data)
        data = re.sub(r"doesn't", "does not",data)
        data = re.sub(r"i'd", "I would", data)
        data = re.sub(r"didn't", "did not", data)
        data = re.sub(r"ain't", "am not", data)
        data = re.sub(r"you'll", "you will", data)
        data = re.sub(r"I've", "I have", data)
        data = re.sub(r"Don't", "do not", data)
        data = re.sub(r"I'll", "I will", data)
        data = re.sub(r"I'd", "I would", data)
        data = re.sub(r"Let's", "Let us", data)
        data = re.sub(r"you'd", "You would", data)
        data = re.sub(r"It's", "It is", data)
        data = re.sub(r"Ain't", "am not", data)
        data = re.sub(r"Haven't", "Have not", data)
        data = re.sub(r"Could've", "Could have", data)
        data = re.sub(r"youve", "you have", data)  
        data = re.sub(r"donå«t", "do not", data)  
        return data

    
    def remove_special_characters(self, data, remove_digits=True):
        pattern=r'[^a-zA-z0-9\s]'
        text=re.sub(pattern,'',data)
        return text
    
    def remove_whitespace(self,data):
        return " ".join(data.split())

    def remove_stopwords(self,data):
        stop_words = set(stopwords.words('english'))
        work_token = word_tokenize(data)
        filter_words = [word for word in work_token if word not in stop_words ]
        filter_text = ''.join(filter_words)
        return filter_text

    def stem_words(self,data):
        stemmer = PorterStemmer()
        word_tokens = word_tokenize(data)
        stems = [stemmer.stem(word) for word in word_tokens]
        stem_text = ' '.join(stems)
        return stem_text

    
    

        
