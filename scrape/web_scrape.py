import bs4 as bs
import urllib.request

from requests import request

class imdb_scrape():
    def __init__(self):
        pass

    def get_rating(self,imdb_id):
        
        sauce = urllib.request.urlopen('https://www.imdb.com/title/{}/ratings/?ref_=tt_ov_rt'.format(imdb_id)).read()
        soup = bs.BeautifulSoup(sauce,'lxml')
        soup_result = soup.find_all('div',attrs={'class':'rightAligned'})
        total_number = soup.find_all('div',attrs={'class':'leftAligned'})
        rating_num = []
        total_num = []
        total_nums = []
        for i in soup_result:
            rating_num.append(i.text)

        for i in total_number:
           
            total_num.append(i.text)
           
        for i in total_num:
          total_nums.append(i.replace(",", ""))
       
        return dict(zip(rating_num,total_nums))

    def dom_rating(self,imdb_id):
        sauce = urllib.request.urlopen('https://www.imdb.com/title/{}/ratings/?ref_=tt_ov_rt'.format(imdb_id)).read()
        soup = bs.BeautifulSoup(sauce,'lxml')
        age = soup.find_all('div',attrs={'class':'tableHeadings'})
        rate_dio = soup.find_all('div',attrs={'class':'bigcell'})
        gender = soup.find_all('div',attrs={'class':'leftAligned'})
        age_data = []
        gender_data = []
        rate_dio_data = []
        for i in age:
            age_data.append(i.text)
            
           
        for i in rate_dio:
            rate_dio_data.append(i.text)
            
        age_data = age_data[2:7]
        rate_dio_data = rate_dio_data[0:5]
        return dict(zip(age_data,rate_dio_data))

    def review(self,imdb_id):
        sauce= urllib.request.urlopen('https://www.imdb.com/title/{}/reviews/?ref_=tt_ql_urv'.format(imdb_id)).read()
        soup = bs.BeautifulSoup(sauce,'lxml')
        price = soup.find_all('div',attrs={'class':'text show-more__control'})
        review = []
        for i in price:
            review.append(i.text)
        return review

    def storyline(self,imdb_id):
        sauce = urllib.request.urlopen('https://www.imdb.com/title/{}/plotsummary?ref_=tt_stry_pl#synopsis'.format(imdb_id)).read()
        soup = bs.BeautifulSoup(sauce,'lxml')
        story = soup.find('ul',attrs={'id':'plot-synopsis-content'})
        
       
        return story.text
        