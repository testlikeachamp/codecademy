import requests

#my_router_ip = "95.174.113.178"
base_url = 'http://httpbin.org/'

def test_httpbin_post():
    mydata = [{'name': 'Artem'}, 'Hi']
    r = requests.post(url=base_url+'post', json=mydata)
    assert r.status_code == 200, r.text
    data = r.json()
    assert data['json'] == mydata


def test_httpbin_ip():
     r = requests.get(url=base_url+'ip')
     assert r.status_code == 200, r.text
     data = r.json()
     #assert data == {u'origin': my_router_ip}
     #print(data)
     if r.elapsed.total_seconds() < 0.500:
         print ('Fast server response = ', r.elapsed.total_seconds(), "\n")

     else:
         print('Long server response = ', r.elapsed.total_seconds(), "\n")

