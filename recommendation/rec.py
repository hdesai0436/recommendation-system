from tracemalloc import stop
import pandas as pd
import numpy as np
from data_ingestion.data_loader import Get_data
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity,linear_kernel
from file_operation.file_methods import file_operations
from api.movieapi import movie_api


class Recommendation(movie_api):
    def __init__(self):
        self.data = Get_data('dataset/main_data.csv').getdata()
       
        super().__init__()

    def get_data_csv(self):
        return self.data

    def read_similarity(self):
        simi = load(self.similarity)
        return simi

    def get_coll_data(self):
        data = Get_data('dataset/coll.csv').getdata()
        return data
    def create_similarity(self):
        try:
            df = self.get_data_csv()
            tf = TfidfVectorizer(stop_words='english',ngram_range=(1,2))
            vector = tf.fit_transform(df['soup'])
            similarity = cosine_similarity(vector,vector)
           
            return similarity
            
        except Exception as e:
            raise Exception (e)

    def content_base_recommnedation(self,movie_name):
        try:
            df = self.get_data_csv()
            simi = self.create_similarity()
            df['title'] = df['title'].apply(lambda x : x.lower())
            
            if movie_name not in df['title'].unique():
                return 'sorry not in the database'
            else:
                idx = df.loc[df['title']==movie_name].index[0]
                sim_scores = list(enumerate(simi[idx]))
                sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
                sim_scores = sim_scores[1:11]
                movie_indices = [i[0] for i in sim_scores]
                l = []
                movies = df.iloc[movie_indices][['title', 'vote_count', 'vote_average']]
                vote_counts = movies[movies['vote_count'].notnull()]['vote_count'].astype('int')
                vote_averages = movies[movies['vote_average'].notnull()]['vote_average'].astype('int')
                C = vote_averages.mean()
                m = vote_counts.quantile(0.20)
                
                qualified = movies[(movies['vote_count'] >= m) & (movies['vote_count'].notnull()) & 
                                (movies['vote_average'].notnull())]
                
                qualified['wr'] = qualified.apply(lambda x: (x['vote_count']/(x['vote_count']+m) * x['vote_average']) + (m/(m+x['vote_count']) * C),axis=1)
                qualified = qualified.sort_values('wr', ascending=False)

                for i in qualified['title']:
                    l.append(i)
                return l
        except Exception as e:
            raise(e)


    

                
    def get_detail_reco_movie(self,movies):
        reco_id = []
        reco_poster=[]
        reco_overview = []
        reco_title = []
        reco_vote_average=[]
        reco_runtime = []
        reco_release_date=[]
        reco_director=[]
        rec_writer = []

        for i in movies:
            id = self.search_movie(i)
            movie_detail = self.movie_detail(id)
            poster = movie_detail['poster_path']
            overview = movie_detail['overview']
            vote_average = movie_detail['vote_average']
            runtime = movie_detail['runtime']
            release_date = movie_detail['release_date']
            title = movie_detail['original_title']
            writer,director = self.dic(id)

            reco_id.append(id)
            reco_poster.append(poster)
            reco_overview.append(overview)
            reco_vote_average.append(vote_average)
            reco_runtime.append(runtime)
            reco_release_date.append(release_date)
            reco_director.append(director)
            reco_title.append(title)
            rec_writer.append(writer)
        return {reco_id[i]:[reco_poster[i],reco_overview[i],reco_vote_average[i],reco_runtime[i],reco_release_date[i],reco_director[i],reco_title[i],rec_writer[i]] for i in range(len(reco_id))}
        




    
