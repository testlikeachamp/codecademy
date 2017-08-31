import requests


my_router_ip = '209.210.253.132'
base_url = 'http://httpbin.org/'


def test_httpbin_post():
    mydata = [{'name': 'Dmitry'}, 'hello']
    r = requests.post(url=base_url+'post', json=mydata)
    assert r.status_code == 200, r.text
    data = r.json()
    assert data['json'] == mydata


def test_httpbin_ip():
    r = requests.get(url=base_url+'ip')
    assert r.status_code == 200, r.text
    data = r.json()
    assert data == {u'origin': my_router_ip}
    # print(data)
    assert r.elapsed.total_seconds() < 0.200
