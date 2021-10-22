import requests
from tmdb import TMDBHelper
from pprint import pprint


def recommendation(title):
    """
    제목에 해당하는 영화가 있으면
    해당 영화의 id를 기반으로 추천 영화 목록을 출력.
    추천 영화가 없을 경우 [] 출력.
    영화 id검색에 실패할 경우 None 출력.
    """
    api_key = '2f3c9cee84d1fd74cfd60f2ddc95418f'
    helper = TMDBHelper(api_key)
    movie_id = helper.get_movie_id(title)
    
    url = helper.get_request_url(method = f'/movie/{movie_id}/recommendations', language = 'ko', region = 'KR')
    response = requests.get(url).json()

    if response.get('success') == False:
        return None
    
    my_list = []
    for res in response['results']:
        my_list.append(res['title'])


    return my_list

if __name__ == '__main__':
    pprint(recommendation('기생충'))
    pprint(recommendation('그래비티'))
    pprint(recommendation('검색할 수 없는 영화'))
