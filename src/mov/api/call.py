def req(dt="20120101"):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = "f3e6e155cfbe1f23ab59dce46ce6818b"
    url = f"{base_url}?key={key}&targetDt={dt}"
    print(url)

