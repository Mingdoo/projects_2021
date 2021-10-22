# 관통 프로젝트 \#1 (pjt01)



## 작성법

- 폴더와 파일명은 영문으로 작성한다.
- [Github-Flavoured Markdown](https://guides.github.com/features/mastering-markdown/) 으로 작성하며 파일 확장자명은 `.md`
- 짧고 간결하며 핵심적인 문장을 사용한다.
- 필요한 설명이 있으면 관련된 정보가 포함된 외부 링크를 사용 하자.

---



##### problem A.

- **조건** :  
  - 제공되는 movie.json 파일을 활용합니다.
  - movie.json은 ‘쇼생크 탈출’ 영화 정보를 가지고 있습니다.

- **결과**
  - 제공된 데이터에서 id, title, poster_path, vote_average, overview, genre_ids 키에 해당하는 정보만 가져옵니다.
  - 가져온 정보를 새로운 dictionary로 반환하는 함수 movie_info를 완성합니다.



<u>**구현한 것**</u> : argument로 들어온 movie_dict 데이터 중에서 필요한 것을 뽑아낸 my_dict를 만든다.

**<u>필요했던 점</u>** : json file의 데이터 타입을 확인하고, python에서 제공하는 key, value 값을 파악하여 key 값으로 value에 접근하여 새로운 dictionary 타입에 저장하고 출력하는 것.

**<u>알고 있던 점</u>** : json 파일을 로드하면 dictionary 타입으로 사용할 수 있다는 것!

**<u>모르고 있던 점</u>** : 새로 들어온 json의 형태를 면밀히 봐야 한다는 것. + pprint 모듈을 사용하여 예~쁘게 출력하기.



---

##### problem B.

- **조건** :
  - 제공되는 movie.json, genres.json 파일을 활용합니다.
  2. movie.json은 ‘쇼생크 탈출’ 영화 정보를 가지고 있습니다.
  3. genres.json은 장르의 id, name 정보를 가지고 있습니다

- **결과** :
  - 제공된 데이터에서 id, title, poster_path, vote_average, overview, genre_ids 키에 해당하는 정보만 가져옵니다.
  - genres.json파일을 이용하여 genre_ids를 genre_names로 변환하여 dictionary에 추가합니다.
  3. 완성된 dictionary를 반환하는 함수 movie_info를 완성합니다.



**<u>구현한 것</u>** : argument로 들어온 movie, genres를 서로 비교하여 movie의 id가 genres의 'id' key의 vaule와 같으면 movie의 id를 genres의 'name' value값으로 바꾸는 것. 간단하게 **숫자가 같으면 숫자를 이름으로 바꿔주는 작업**.

**<u>필요했던 점</u>** : 두 dictionary 타입의 비교를 헷갈리지 않게 인덱스로 접근하는 것. 또는 `dict.items()`로 접근해서 데이터를 가져오는 것도 좋은 방법일 것 같음.

**<u>알고 있던 점</u>** : dictionary 타입을 key로 접근하는 것.

**<u>모르고 있던 점</u>** :



---

##### problem C.

- **조건** :
  - 제공되는 movies.json, genres.json 파일을 사용합니다.
  2. movies.json은 영화 전체 정보를 가지고 있습니다.
  3. genres.json은 장르의 id, name 정보를 가지고 있습니다.

- **<u>결과</u>** : 
  - 이전 단계의 함수 구조를 재사용합니다.
  2. 영화 전체 정보를 수정하여 반환하는 함수 movie_info를 완성합니다.



**<u>구현한 것</u>** : #B에서 진행했던 장르 이름 매칭을 여러 영화에 대해 매칭시키는 것.

**<u>필요했던 점</u>** : for문 또는 while문과 같은 반복문을 사용하여 모든 영화에 대해 접근하고 필요한 정보를 받아와서 출력하는 것.

**<u>알고있던 점</u>** : for문을 사용해서 모든 영화에 접근하는 것.

**<u>모르고 있던 점</u>** : 



---

##### problem D.

- **<u>조건</u>** : 
  - movies.json과 movies폴더 내부의 파일들을 사용합니다.
  2. movies.json은 영화 전체 데이터를 가지고 있습니다.
  3. movies 폴더 내부의 파일들은 각 영화의 상세정보를 가지고 있습니다.
  3. 수익정보는 상세정보 파일을 통해 확인 할 수 있습니다.
- **<u>결과</u>** :
  - 수익이 가장 높은 영화의 제목을 출력하는 함수 max_revenue를 완성합니다.



**<u>구현한 것</u>** : '\data\movies\' 내에 있는 모든 `.json`파일을 가져와 **revenue**의 값을 비교하고, 가장 큰 값을 가지는 영화의 제목을 출력하는 것.

**<u>필요했던 점</u>** : '\data\movies' 디렉토리 내에 있는 모든 파일을 파이썬으로 읽어내고 분석하는 것.

**<u>알고있던 점</u>** : #B, #C에서 했던 인덱스를 통한 접근, key value의 접근

**<u>모르고 있던 점</u>** : os 모듈로 디렉토리 내의 모든 파일을 list형태로 뽑아올 수 있다는 것.

```python
json_files = 
[my_file for my_file in os.listdir('data/movies') if my_file.endswith('.json')]

#문법.
[<name> for <name> in <iterable> if <condition>] #여기서 if condition은 빠져도 됨.

#os.listdir
os.listdir('path') => list(str)
```



---

##### problem E.

- **<u>조건</u>** : 
  - movies.json과 movies폴더 내부의 파일들을 사용합니다.
  2. movies.json은 영화 전체 데이터를 가지고 있습니다.
  3. movies 폴더 내부의 파일들은 각 영화의 상세정보를 가지고 있습니다.
  3. 개봉일 정보는 상세정보 파일을 통해 확인 할 수 있습니다.
- 결과
  - 개봉일이 12월인 영화들의 제목을 리스트로 출력하는 함수 dec_movies를 완성합니다.



**<u>구현한 것</u>** : #D에서 구현한 것과 같이 디렉토리 내에 있는 모든 json파일을 불러와 분석하고 원하는 데이터를 뽑아 출력해내는 것.

**<u>필요했던 점</u>** : '\data\movies' 디렉토리 내에 있는 모든 파일을 파이썬으로 읽어내고 분석하는 것.

**<u>알고있던 점</u>** : for문을 사용한 인덱스를 통한 접근

**<u>모르고 있던 점</u>** : 

---

## 코드 첨부

#C, #E는 각각 problem A,B,C의 합집합, problem D,E의 합집합이다. 문제 C,E의 코드를 첨부한다.



##### problem C.

```python
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
```



##### problem E.

```python
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
```



