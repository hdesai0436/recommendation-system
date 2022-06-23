
from data_ingestion.data_loader import Get_data
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from api.movieapi import movie_api


class TVRecomend(movie_api):
    def __init__(self):
        self.data = Get_data('dataset/netflix_titles.csv').getdata()
        
        super().__init__()

    def get_data_csv(self):
        return self.data


    def get_tv_show_data(self):
        df = self.get_data_csv()
        tv = df[df['type'] == 'TV Show']
        tv = tv.fillna("")
        return tv
    
    def create_soup(self,x):
        return x['title']+ ' ' + x['director'] + ' ' + x['cast'] + ' ' +x['listed_in']+' '+ x['description']

    def select_feature(self):
        df = self.get_tv_show_data()
        df = df[['title','director','cast','listed_in','description']]
        df['soup'] = self.create_soup(df)
        df['soup'] = df['soup'].apply(lambda x:x.lower())
        df['soup'] = df['soup'].apply(lambda x:x.replace(" ",""))
        
        return df

    def create_similarity(self):
        df = self.select_feature()
        tf = TfidfVectorizer(stop_words='english',ngram_range=(1,1))
        vector = tf.fit_transform(df['soup'])
        simi = cosine_similarity(vector,vector)
        return simi
       


    def tv_show_content_base(self,title):
        reco_show = []
        df = self.select_feature()
        simi = self.create_similarity()
        df['title'] = df['title'].apply(lambda x: x.lower())

        if title not in df['title'].unique():
            return 'not tv show in dataset'
        else:
            fa = df.reset_index()
            indices = pd.Series(fa.index, index=fa['title'])
            idx = indices[title]
            # Get the pairwsie similarity scores of all movies with that movie
            sim_scores = list(enumerate(simi[idx]))

            # Sort the movies based on the similarity scores
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

            # Get the scores of the 10 most similar movies
            sim_scores = sim_scores[1:11]

            # Get the movie indices
            movie_indices = [i[0] for i in sim_scores]

            # Return the top 10 most similar movies
            
            t = df['title'].iloc[movie_indices]
            new_l = t.tolist()
            
            return new_l
           
    def reco_show_detail(self,movies):
        tv_reco_id = []
        tv_reco_poster=[]
        tv_reco_overview = []
        tv_reco_title = []
        tv_reco_vote_average=[]
        tv_reco_runtime = []
        tv_reco_release_date=[]
        tv_reco_director=[]
        try:
            for i in movies:
                tv_id = self.search_tv_show(i)
                tv_detail = self.show_detail(tv_id)
                created_by,genres = self.show_created_genres(tv_id)
                tv_reco_title.append(tv_detail['original_name'])
                tv_reco_vote_average.append(tv_detail['vote_average'])
                tv_reco_overview.append(tv_detail['overview'])
                tv_reco_poster.append(tv_detail['poster_path'])
                tv_reco_runtime.append(tv_detail['episode_run_time'])
                tv_reco_release_date.append(tv_detail['first_air_date'])
                tv_reco_id.append(tv_detail['id'])
                tv_reco_director.append(created_by)
            return {tv_reco_id[i]:[tv_reco_poster[i],tv_reco_title[i],tv_reco_vote_average[i],tv_reco_overview[i],tv_reco_runtime[i],tv_reco_release_date[i],tv_reco_director[i]] for i in range(len(tv_reco_id))}
        except Exception as e:
            raise(e)







    

    
    
