import json
from pprint import pp, pprint
import os

def max_revenue(movies):
    movie_ids=[]
    for i in range(len(movies)):
        movie_ids.append(movies[i]['id'])
    
    json_files = [my_file for my_file in os.listdir('data/movies') if my_file.endswith('.json')]
    json_data = []
    for json_file in json_files:
        cur_json = open('data/movies/'+json_file, encoding='UTF8')
        json_data.append(json.load(cur_json))

    max_revenue = json_data[0]['revenue']
    for j in range(len(movies)):
        if json_data[j]['revenue'] > max_revenue:
            max_revenue = json_data[j]['revenue']
            idx = j
    
    max_revenue_movie = json_data[idx]

    return max_revenue_movie['title']
    

    
 
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))