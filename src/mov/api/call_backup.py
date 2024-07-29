import requests
import os
import pandas as pd
from datetime import datetime

def save2df(load_dt='20120101'):
    """airflow 호출 지점"""
    df = list2df(load_dt)
    # date = datetime.now().strftime("%Y%m%d")
    # df에 load_Dt 칼럼 추가 조회 일자 YYYYMMDD 형식으로 
    # df['load_dt'] = date
    df['load_dt'] = '20120101'
    print(df.head(5))
    
    # load_Dt 기본으로 partitioning
    df.to_parquet("~/tmp/test_parquet/", partition_cols=['load_dt'])
    return df 

def list2df(load_dt='20120101'):
    l = req2list(load_dt)
    df = pd.DataFrame(l)
    return df

def req2list(load_dt='20120101') -> list:
    _, data = req(load_dt)
    l = data['boxOfficeResult']['dailyBoxOfficeList']
    '''
    for movie in l:
        print("\n")
        for info in movie:
            print(f'{info} : {movie[info]}') 
    '''
    return l 

def get_key():
    """영화진흥위원회 가입 및 API KEY 생성 후 환경변수 선언 필요"""
    key = os.getenv('MOVIE_API_KEY')
    return key

def req(load_dt="20120101"):
    url = gen_url(load_dt)
    r = requests.get(url)
    
    code = r.status_code
    data = r.json()
    return code, data

def gen_url(dt="20120101"):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = get_key()
    url = f"{base_url}?key={key}&targetDt={dt}"
    
    return url
