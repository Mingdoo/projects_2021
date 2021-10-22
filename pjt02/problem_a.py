import requests
from tmdb import TMDBHelper
from pprint import pprint

def popular_count():
    api_key = '2f3c9cee84d1fd74cfd60f2ddc95418f'
    helper = TMDBHelper(api_key)
    url = helper.get_request_url()
    response = requests.get(url).json()
    
    pprint(response)
    return len(response['results'])

if __name__ == '__main__':
    print(popular_count())
