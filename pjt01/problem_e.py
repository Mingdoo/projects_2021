import json
import os

def dec_movies(movies):

    #movies 디렉토리 내에 있는 모든 json파일들을 가져온다. 
    json_files = [my_file for my_file in os.listdir('data/movies') if my_file.endswith('.json')]
    json_data = []
    for json_file in json_files:
        #여기서 json_data에 모든 영화 세부정보를 담아온다.
        cur_json = open('data/movies/'+json_file, encoding='UTF8')
        json_data.append(json.load(cur_json))

    #조건문을 통해 12월에 release된 영화들의 index를 뽑아온다.
    my_idx=[]
    for j in range(len(movies)):
        if json_data[j]['release_date'][5:7] == '12':
            my_idx.append(j)

    #뽑아온 index를 사용하여 title정보를 Release_in_Dec 리스트에 저장한다.
    Release_in_Dec = []
    for idx in my_idx:
        Release_in_Dec.append(json_data[idx]['title'])

    return Release_in_Dec
    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))