
import requests
import os
from dotenv import load_dotenv

load_dotenv()


class movie_api():
    def __init__(self):
        self.api = os.getenv('TMDB_API_KEY')

    def search_movie(self,movie_name):
        '''
        This Function get movie id base on user search
        '''
        try:
            re = requests.get('https://api.themoviedb.org/3/search/movie?api_key='+self.api+'&language=en-US&query='+movie_name+'&page=1&include_adult=false')
            response = re.json()
            return response['results'][0]['id']
        except Exception as e:
            raise Exception("din't find any movie with that name" + str(e))

    def movie_detail(self,movie_id):
        try:
            re = requests.get('https://api.themoviedb.org/3/movie/'+str(movie_id)+'?api_key='+self.api+'&language=en-US')
            movie_json= re.json()
            return movie_json
        except Exception as e:
            raise Exception ('There is no movie detail for id that user search ' + str(e))

    def get_movie_cast(self,movie_id,type):
        cast_id = []
        cast_name = []
        cast_char = []
        cast_profile = []
        top_10 = [0,1,2,3,4,5,6,7,8,9]
        re = requests.get('https://api.themoviedb.org/3/'+type+'/'+str(movie_id)+'/credits?api_key='+self.api+'&language=en-US')
        cast_res = re.json()
        if len(cast_res['cast']) >= 10:
            top_10 = [0,1,2,3,4,5,6,7,8,9]
        else:
            top_10 = [0,1,2,3,4]

        for i in top_10:
            cast_id.append(cast_res['cast'][i]['id'])
            cast_name.append(cast_res['cast'][i]['name'])
            cast_char.append(cast_res['cast'][i]['character'])
            cast_profile.append(cast_res['cast'][i]['profile_path'])
        return {cast_id[i]:[cast_name[i],cast_char[i],cast_profile[i]] for i in range(len(cast_id))}

    def person_detail(self,movie_id):
        person = self.get_movie_cast(movie_id,'movie')
        person_name = []
        person_birthday = []
        person_biography = []
        person_birth_place = []
        person_popularity = []
        person_profile = []
        
        for i,k in person.items():
            re = requests.get('https://api.themoviedb.org/3/person/'+str(i)+'?api_key='+self.api+'&language=en-US')
            person_res= re.json()
            if person_res['birthday']:

                person_birthday.append(person_res['birthday'])
            else:
                person_birthday.append('Information not aviable')

            if person_res['biography']:

                person_biography.append(person_res['biography'])
            else:
                person_biography.append('no bio avivbale')
            if person_res['place_of_birth']:

                person_birth_place.append(person_res['place_of_birth'])
            else:
                person_birth_place.append('no birthday')
            
            if person_res['popularity']:

                person_popularity.append(person_res['popularity'])
            else:
                person_popularity.append('no popularoty')
            if k[0]:
                person_name.append(k[0])
            else:
                person_name.append('no name')
            if k[2]:
                person_profile.append(k[2])
            else: 
                person_profile.append('no prifle')
        return {person_name[i]:[person_birthday[i],person_biography[i],person_birth_place[i],person_profile[i]] for i in range(len(person_name))}

    def dic(self,movie_id):
        re = requests.get('https://api.themoviedb.org/3/movie/'+str(movie_id)+'/credits?api_key='+self.api+'&language=en-US')
        dic = re.json()
        for i in dic['crew']:
            if i['department'] == 'Writing':
                writer = i['name']
                break
        for i in dic['crew']:
            if i['department'] == 'Directing':
                director = i['name']
                break
        

        return writer,director

    def movie_video(self,movie_id):
        re = requests.get('https://api.themoviedb.org/3/movie/'+str(movie_id)+'/videos?api_key='+self.api+'&language=en-US')
        movie_videos = re.json()
        return movie_videos['results']

    def serach_people(self,person_name):
        try:
            re = requests.get("https://api.themoviedb.org/3/search/person?api_key="+self.api+"&language=en-US&query="+person_name+"&page=1&include_adult=false")
            person = re.json()
            
            if person:
                try:
                    person_id = person['results'][0]['id']
                    print(person_id)
                    return str(person_id)
                except Exception as e:
                    return (e)
        except Exception as e:
            raise(e)

    def detail_person(self,person_id):
        actor_name = []
        actor_image = []
        actor_bio = []
        actor_birth_date = []
        place_birth = []
        try:
            re = requests.get("https://api.themoviedb.org/3/person/"+ person_id + "?api_key="+self.api + "&language=en-US")
            res = re.json()
            if res['birthday']:
                actor_birth_date.append(res['birthday'])
            else: 
                actor_birth_date.append('infomation not aviable')
            if res['name']:
                actor_name.append(res['name'])
            else:
                actor_name.append('infomation not aviable')
            if res['profile_path']:
                actor_image.append(res['profile_path'])
            else:
                actor_image.append('infomation not aviable')
            if res['biography']:
                actor_bio.append(res['biography'])
            else:
                actor_bio.append('infomation not aviable')
            if res['place_of_birth']:
                place_birth.append(res['place_of_birth'])
            else:
                place_birth.append('not aviable')
            return {actor_name[i]:[actor_image[i],actor_bio[i],actor_birth_date[i],place_birth[i]] for i in range(len(actor_name))}
            
        except Exception as e:
            raise (e) + 'desvoi'




    def person_films(self,person_id):
        try:
            re = requests.get('https://api.themoviedb.org/3/person/'+str(person_id)+'/movie_credits?api_key='+self.api+'&language=en-US')
            res = re.json()
            movie_name = []
            releae_date = []
            character_film = []
            poster_path = []
           
            if res:
                try:
                    for i in res['cast']:
                        movie_name.append(i['title'])
                        
                        if i.get('release_date'):
                            releae_date.append(i['release_date'])
                        else:
                            releae_date.append('not')
                        character_film.append(i['character'])
                        poster_path.append(i['poster_path'])
                    return {movie_name[i]:[releae_date[i],character_film[i],poster_path[i]] for i in range(len(movie_name))}

                except Exception as e:
                    raise(e)
           
        except Exception as e:
            raise(e)
                


    def get_type_movie(self,type_movie):
        popular_movie_name = []
        popular_id = []
        popular_vote_average = []
        popular_poster = []
        popular_video = []
        re = requests.get('https://api.themoviedb.org/3/movie/'+type_movie+'?api_key='+self.api+'&language=en-US&region=US')
        popular_movie = re.json()
       
        for i in popular_movie['results']:
            popular_movie_name.append(i['original_title'])
            popular_id.append(i['id'])
            popular_vote_average.append(i['vote_average'])
            popular_poster.append(i['poster_path'])

        for i in popular_id:
            re = requests.get('https://api.themoviedb.org/3/movie/'+str(i)+'/videos?api_key='+self.api+'&language=en-US')
            movie_videos = re.json()
            try:
                if movie_videos['results']:
                    popular_video.append(movie_videos['results'][0]['key'])
                else:
                    popular_video.append('none')

            except Exception as e:
                raise(e)
                

        return {popular_id[i]:[popular_movie_name[i],popular_vote_average[i],popular_poster[i],popular_video[i]] for i in range(len(popular_id))}


    def trading_actors(self):
        actor_name = []
        actor_profile = []
        actor_work = []
        try:
            re = requests.get('https://api.themoviedb.org/3/trending/person/day?api_key='+ self.api)
            res = re.json()
            for i in res['results']:
                actor_name.append(i['name'])
                actor_profile.append(i['profile_path'])
                actor_work.append(i['known_for_department'])

            return {actor_name[i]:[actor_profile[i],actor_work[i]] for i in range(len(actor_name))}

        except Exception as e:
            raise e

    def search_tv_show(self,show_name):
        try:
            re = requests.get('https://api.themoviedb.org/3/search/tv?api_key='+self.api + '&language=en-US&page=1&query='+show_name+'&include_adult=false')
            res = re.json()
            for i in res['results']:
                return i['id']
                break
        except Exception as e:
            raise(e)
            
    def show_detail(self,show_id):

        try:
            re = requests.get('https://api.themoviedb.org/3/tv/'+str(show_id)+'?api_key='+self.api+'&language=en-US')
            res = re.json()
            return res
        except Exception as e:
            raise(e)
    
    def show_created_genres(self,show_id):
        created_name = []
        show_genres = []
        try:
            re = requests.get('https://api.themoviedb.org/3/tv/'+str(show_id)+'?api_key='+self.api+'&language=en-US')
            res = re.json()
            for i in res['created_by']:
                created_name.append(i['name'])
            for i in res['genres']:
                show_genres.append(i['name'])
           
            return created_name,show_genres
        except Exception as e:
            raise(e)

    def show_genres(self,show_id):
        show_genres = []
        try:
            re = requests.get('https://api.themoviedb.org/3/tv/'+str(show_id)+'?api_key='+self.api+'&language=en-US')
            res = re.json()
            for i in res['genres']:
                show_genres.append(i['name'])
            return show_genres
        except Exception as e:
            raise(e)

    def session(self,show_id):
        tv_show_poster = []
        number_episod = []
        show_name = []
        air_date = []
        session_id = []
        session_number = []
        try:
            re = requests.get('https://api.themoviedb.org/3/tv/'+str(show_id)+'?api_key='+self.api+'&language=en-US')
            res = re.json()
            for i in res['seasons']:
                tv_show_poster.append(i['poster_path'])
                number_episod.append(i['episode_count'])
                show_name.append(i['name'])
                air_date.append(i['air_date'])
                session_id.append(i['id'])
                session_number.append(i['season_number'])


            return {session_id[i]:[tv_show_poster[i],number_episod[i],show_name[i],air_date[i],session_number[i]] for i in range(len(session_id))}
        except Exception as e:
            raise(e)



        
    