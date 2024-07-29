# mov

### install
```
# main
$ pip install git+https://github.com/Seokxkyu/mov.git
```

### start development
```sh
$ git clone <URL>
$ cd <DIR>
$ source .venv/bin/activate
$ pdm install

$ pytest

# option
$ pdm venv create
```


### setting environment
```bash
cat ~/.zshrc | tail -n 3


# MY_ENV
export MOVIE_API_KEY=<KEY>
```

### error guide
- [ ] 영화진흥위원회 가입 API KEY 발급 및 환경변수 추가 
```
{'faultInfo': {'messsage': '유효하지않은 키값입니다.', 'errorCode': ''}}
```
