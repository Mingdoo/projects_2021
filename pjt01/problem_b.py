import json
from pprint import pprint


def movie_info(movie, genres):
    my_dict = dict(
        genre_ids = movie['genre_ids'],
        id = movie['id'],
        overview = movie['overview'],
        poster_path = movie['poster_path'],
        title = movie['title'],
        vote_average = movie['vote_average'],    
    )
    
    for i in range(len(my_dict['genre_ids'])):
        for j in range(len(genres)):
            if my_dict['genre_ids'][i] == genres[j]['id']:
                my_dict['genre_ids'][i] = genres[j]['name']
    return my_dict

    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))