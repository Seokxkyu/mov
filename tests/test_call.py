# test_call.py

from mov.api.call import gen_url, req

def test_url_test():
    url = gen_url()

    assert "http" in url

def test_req():
    code, data = req()
    assert code == 200

    code, data = req('20240710') 
    assert code == 200
