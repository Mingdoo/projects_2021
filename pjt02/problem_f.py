from pprint import pprint
import requests

def boxoffice(yyyymmdd):

    url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'
    
    key = '471d01a31185dc4de8bb2a698a0003b1'
    date = str(yyyymmdd)
    
    url += '&key='+key
    url += '&targetDt='+date
    response = requests.get(url).json()

    my_list1 = []
    my_list2 = []
    for movie in response['boxOfficeResult']['dailyBoxOfficeList']:
        my_list1.append(movie['movieNm'])
        my_list2.append(movie['audiAcc'])
    
    print(my_list1)
    print(my_list2)
    my_dict = dict(zip(my_list1, my_list2))
    return my_dict

if __name__ == '__main__':
    pprint(boxoffice(20210729))