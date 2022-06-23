import requests
class Imdb_data():
    def __init__(self):
        self.headers = {
            "X-RapidAPI-Host": "imdb8.p.rapidapi.com",
            "X-RapidAPI-Key": "013eca4e62msh0076a0f914a6825p109ce0jsne3ad41422ac1"
        }

    def BoxOffice(self,imdb_id):
        url = "https://imdb8.p.rapidapi.com/title/v2/get-business"
       
        querystring = {"tconst":imdb_id}
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        r = response.json()
        res = r['titleBoxOffice']['gross']['regional']
        cost  = []
        region = []
        for i in res[0:11]:
            for k,v in i.items():
                if k == 'total':
                    cost.append(v['amount'])
                if k == 'regionName':
                    region.append(v)
        res_weekend = r['titleBoxOffice']['openingWeekendGross']['regional']
        weekend_cost = []
        weekend_region = []
        for i in res_weekend[0:11]:
            for k,v in i.items():
                if k == 'total':
                    weekend_cost.append(v['amount'])
                if k == 'regionName':
                    weekend_region.append(v)

        return dict(zip(region,cost)),dict(zip(weekend_region,weekend_cost))

    def news(self,imdb_id):
        url = "https://imdb8.p.rapidapi.com/title/get-news"
        querystring = {"tconst":imdb_id}
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        r = response.json()
        new = r['items'][0:5]
        renews = {}
        for i in new:
            renews[i['head']] = i['link'],i['image']['url']
        return renews
           



