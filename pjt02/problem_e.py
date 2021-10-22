import requests
from tmdb import TMDBHelper
from pprint import pprint


def credits(title):
    """
    제목에 해당하는 영화가 있으면
    해당 영화 id를 통해 영화 상세정보를 검색하여
    주연배우 목록과 목록을 출력.
    영화 id검색에 실패할 경우 None 출력.
    """
    api_key = '2f3c9cee84d1fd74cfd60f2ddc95418f'
    helper = TMDBHelper(api_key)
    movie_id = helper.get_movie_id(title)
    
    url = helper.get_request_url(method = f'/movie/{movie_id}/credits', language = 'ko', region = 'KR')
    response = requests.get(url).json()

    if response.get('success') == False:
        return None
        
    actor_list = []

    for res in response['cast']:
        if res['cast_id'] < 10:
            actor_list.append(res['name'])
    
    crew_list = []
    
    for crew in response['crew']:
        if crew['department'] == 'Directing':
            crew_list.append(crew['name'])
    
    my_dict = {'cast' : actor_list, 'crew' : crew_list}

    return my_dict


if __name__ == '__main__':
    pprint(credits('기생충'))
    pprint(credits('검색할 수 없는 영화'))
