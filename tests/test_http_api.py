# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests

#my_router_ip = "95.174.113.178"
base_url = 'http://localhost:8000/'
#base_url = 'http://httpbin.org/'

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
         print ('Быстрый ответ сервера = ', r.elapsed.total_seconds(), "\n")

     else:
         print('Долгий ответ сервера :( = ', r.elapsed.total_seconds(), "\n")


def test_httpbin_user_agent():
    r = requests.get(base_url + 'user-agent')
    assert r.status_code == 200, r.text
    assert r.reason == "OK", r.text
    assert r.json()['user-agent'] == 'python-requests/' + requests.__version__
    print(r.elapsed.total_seconds())
    #data = r.json()
    #assert len(r.json())
    #print(data)
    #print(r.reason)
