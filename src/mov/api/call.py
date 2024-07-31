import requests
import os
import pandas as pd

def echo(yaho):
    return yaho

# parquet 불러와 상수 컬럼의 경우 타입 변환하기
def apply_type2df(load_dt='20120101', path="~/tmp/test_parquet"):
    df = pd.read_parquet(f"{path}/load_dt={load_dt}")
    num_cols = ['rnum', 'rank', 'rankInten', 'salesAmt', 'audiCnt', 'audiAcc', 'scrnCnt', 'showCnt', 'salesShare', 'salesInten', 'salesChange', 'audiInten', 'audiChange']

    for col in num_cols:
        df[col] = pd.to_numeric(df[col])
    return df

# 데이터프레임에 load_dt 컬럼 추가하고 parquet로 변환하기
def save2df(load_dt='20120101', url_param={}):
    """airflow 호출 지점"""
    df = list2df(load_dt, url_param)
    df['load_dt'] = load_dt
    # print(df.head(5))
    
    # load_Dt 기본으로 partitioning
    df.to_parquet("~/tmp/test_parquet/", partition_cols=['load_dt'])
    return df 

# 변환한 리스트 데이터프레임으로 변환하기 
def list2df(load_dt='20120101', url_param={}):
    l = req2list(load_dt, url_param)
    df = pd.DataFrame(l)
    return df

# 받아온 json 데이터에서 리스트 추출하기 
def req2list(load_dt='20120101', url_param={}) -> list:
    code, data = req(load_dt, url_param)
    l = data['boxOfficeResult']['dailyBoxOfficeList']
    print(f"API Response Code: {code}")
    print(f"API Response Data for {url_param}: {data}")

    return l 

def get_key():
    """영화진흥위원회 가입 및 API KEY 생성 후 환경변수 선언 필요"""
    key = os.getenv('MOVIE_API_KEY')
    return key

# URL 요청하여 데이터 받아오기 (받아오는 데이터 형식은 json)
def req(load_dt="20120101", url_param={}):
    url = gen_url(load_dt, url_param)
    r = requests.get(url)
    
    code = r.status_code
    data = r.json()
    return code, data

# 날짜와 파라미터 설정하여 URL 만들기
def gen_url(dt="20120101", url_param={"multiMovieYn": "N"}):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = get_key()
    url = f"{base_url}?key={key}&targetDt={dt}"
    
    for key, value in url_param.items():
        # url = url + "&multiMovieYn=Y"
        url = url + f"&{key}={value}"
    
    print("*^=" * 10)
    print(url)
    print("*^=" * 10)
    return url

    return url
