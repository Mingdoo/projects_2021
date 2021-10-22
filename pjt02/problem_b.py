import requests
from tmdb import TMDBHelper
from pprint import pprint


def vote_average_movies():
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 출력.
    """
    api_key = '2f3c9cee84d1fd74cfd60f2ddc95418f'
    helper = TMDBHelper(api_key)
    url = helper.get_request_url()
    movies = requests.get(url).json()

    my_list = []
    my_list2 = []
    for movie in movies['results']:
        if movie['vote_average'] >= 8:
            my_list.append(movie['overview'])
            my_list2.append(movie['title'])

    my_dict = dict(zip(my_list2, my_list))
    return my_dict
    
    

if __name__ == '__main__':
    pprint(vote_average_movies())
