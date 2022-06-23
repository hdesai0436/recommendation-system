
from flask import Blueprint, jsonify, redirect,render_template,flash,url_for,request


from scrape.web_scrape import imdb_scrape

from api.movieapi import movie_api

from imdb_api.imdb import Imdb_data
from text_preprocess.text_pre import text_processing
from file_operation.file_methods import file_operations
import numpy as np
from summary.summar import Text_summary

from recommendation.rec import Recommendation
import pandas as pd
from tvshow.tv_show_reco import TVRecomend
views = Blueprint('views',__name__)
cv = file_operations().load_model('tran')
lg_model = file_operations().load_model('logis')





@views.route('/')
def home():
    data = movie_api()
    movie_popular = data.get_type_movie('popular')
    top_rated = data.get_type_movie('top_rated')
    up_coming = data.get_type_movie('upcoming')
    thre =  data.get_type_movie('now_playing')
    
    
    return render_template('index.html',movie_popular=movie_popular,top_rated=top_rated,up_coming=up_coming,thre=thre)

@views.route('/movie/<name>')
def movie(name):
   
    try:
        api = movie_api()
        imdb_api = Imdb_data()
        imdb_data = imdb_scrape()
        id = api.search_movie(name)
        
        movie_details = api.movie_detail(id)
        imdb_id = movie_details['imdb_id']
        
        title = movie_details['original_title'].lower()
        poster = movie_details['poster_path']
        overview = movie_details['overview']
        budget = movie_details['budget']
        runtime = movie_details['runtime']
        release_date = movie_details['release_date']
        vote_average = movie_details['vote_average']
        vote_count = movie_details['vote_count']
        
        income,weekend_income = imdb_api.BoxOffice(imdb_id)
        
        rating_num = imdb_data.get_rating(imdb_id)

        age_rate = imdb_data.dom_rating(imdb_id)
        relate_news = imdb_api.news(imdb_id)
        writer,director = api.dic(id)
        actors_info = api.person_detail(id)

        movie_video = api.movie_video(id)
        
        
        movie_review = imdb_data.review(imdb_id)
        
        storyline = imdb_data.storyline(imdb_id)
        reco_movie = Recommendation().content_base_recommnedation(name)
        reco_detail = Recommendation().get_detail_reco_movie(reco_movie)
        review_list = []
        review_status=[]
        summary_review = []

        for i in movie_review:
            review_list.append(i)
            summary = Text_summary(i).genrate_summary()
            summary_review.append(summary)
               
            movie_review_list = np.array([i])
            text_pre = text_processing().text_preprocese(movie_review_list)
            
            movie_vector = cv.transform(text_pre)
            pred = lg_model.predict(movie_vector)
            review_status.append(pred)
            
        movie_reviews = {review_list[i]: [review_status[i],summary_review[i]] for i in range(len(review_list))}  
        return render_template('moviedetail.html', title = title,poster=poster,overview=overview,budget=budget,runtime=runtime,release_date=release_date,
                               vote_average=vote_average,vote_count=vote_count,income=income,weekend_income=weekend_income,rating_num=rating_num,age_rate=age_rate,relate_news=relate_news,writer=writer,director=director,
                                actors_info=actors_info,movie_video=movie_video,storyline=storyline,reco_detail=reco_detail,movie_reviews=movie_reviews )
        
        
        
            
    except Exception as e:
        raise(e)
        # flash('Post cannot be empty')
        # return redirect(url_for('views.home'))
        

@views.route('/actor/<string:actor_name>')
def actor_view(actor_name):
    
    try:
        
        tmdb_api = movie_api()
        person_id = tmdb_api.serach_people(actor_name)
        person_detail = tmdb_api.detail_person(person_id)
        all_movie_by_person = tmdb_api.person_films(person_id)
        return render_template('actor.html',person_detail=person_detail,all_movie_by_person=all_movie_by_person)
            
      
    except Exception as e:
        raise e 

@views.route('/actors')
def actors():
   
    api = movie_api()
    trand_people = api.trading_actors()
    return render_template('list_actor.html',trand_people=trand_people)

@views.route('/tvshow/<show_name>')
def tv_show(show_name):
    api = movie_api()
    recomend = TVRecomend()
    tv_show_id = api.search_tv_show(show_name=show_name)
    tv_show_detail = api.show_detail(tv_show_id)
    overview = tv_show_detail['overview'] 
    poster_path = tv_show_detail['poster_path']
    vote_average = tv_show_detail['vote_average']
    vote_count = tv_show_detail['vote_count']
    original_name = tv_show_detail['original_name']
    casts = api.get_movie_cast(tv_show_id,'tv')
    created_by,genres = api.show_created_genres(tv_show_id)
    session = api.session(tv_show_id)
    first_air_date = tv_show_detail['first_air_date']
    runtime = tv_show_detail['episode_run_time'][0]
    tv_reco = TVRecomend().tv_show_content_base(show_name)
    tv_reco_detail = TVRecomend().reco_show_detail(tv_reco)


    return render_template('tv_show.html',casts = casts,original_name=original_name,overview=overview,poster_path=poster_path,vote_average=vote_average,vote_count=vote_count,
                            created_by=created_by,genres=genres,session=session,first_air_date=first_air_date,runtime=runtime,tv_reco_detail=tv_reco_detail)











            








    