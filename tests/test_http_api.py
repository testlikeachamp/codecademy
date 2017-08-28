import requests

my_router_ip = "95.174.113.178"
base_url = 'http://httpbin.org/'

def test_httpbin_post():
    mydata = [{'name': 'Artem'}, 'Hi']
    r = requests.post(url=base_url+'post', json=mydata)
    assert r.status_code == 200, r.text
    data = r.json()
    assert data['json'] == mydata