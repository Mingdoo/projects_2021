import json
from pprint import pprint


def movie_info(movies, genres):
    my_list = []
    #인덱스로 접근하여 movies 데이터에 접근한다.
    for i in range(len(movies)):
        my_dict = dict(
        genre_ids = movies[i]['genre_ids'],
        id = movies[i]['id'],
        overview = movies[i]['overview'],
        poster_path = movies[i]['poster_path'],
        title = movies[i]['title'],
        vote_average = movies[i]['vote_average'],    
        )
        #genres와 movie의 id를 비교하여 새로운 데이터를 만든다(my_list)
        for i in range(len(my_dict['genre_ids'])):
            for j in range(len(genres)):
                if my_dict['genre_ids'][i] == genres[j]['id']:
                    my_dict['genre_ids'][i] = genres[j]['name']
        my_list.append(my_dict)
    return my_list
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))