import requests

def req(dt="20120101"):
    # url = gen_url('20240720')
    url = gen_url(dt)
    r = requests.get(url)
    
    code = r.status_code
    data = r.json()
    print(data)
    return code, data

def gen_url(dt="20120101"):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = "f3e6e155cfbe1f23ab59dce46ce6818b"
    url = f"{base_url}?key={key}&targetDt={dt}"
    
    return url
