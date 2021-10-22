import requests
from tmdb import TMDBHelper
from pprint import pprint


def ranking():
    """
    popular 영화목록을 정렬하여 평점순으로 5개 출력.
    """
    api_key = '2f3c9cee84d1fd74cfd60f2ddc95418f'
    helper = TMDBHelper(api_key)
    url = helper.get_request_url(language='ko', region = 'KR')
    response = requests.get(url).json()

    dict_sorted = sorted(response['results'], reverse=True, key=(lambda item: item['vote_average']))

    pprint(dict_sorted[:5])


if __name__ == '__main__':
    pprint(ranking())

