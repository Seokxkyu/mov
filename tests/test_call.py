# test_call.py

from mov.api.call import gen_url, req, get_key, req2list, list2df, save2df
# from mov.api.call import *
import pandas as pd

def test_save2df():
    df = save2df()
    assert isinstance(df, pd.DataFrame)
    assert 'load_dt' in df.columns
    # df = save2df(load_dt='20240101')

def test_list2df():
    df = list2df()
    assert isinstance(df, pd.DataFrame)
    assert 'rnum' in df.columns
    assert 'movieNm' in df.columns

def test_req2list():
    l = req2list()
    assert len(l) > 0
    v = l[0]
    assert 'rnum' in v.keys()
    assert v['rnum'] == '1'

def test_get_key():
    key = get_key()
    assert key

def test_url_test():
    url = gen_url()
    assert "http" in url
    url = gen_url('20241231')
    assert '20241231' in url

def test_req():
    """
    code, data = req()
    assert code == 200
    """
    code, data = req('20240710') 
    assert code == 200
