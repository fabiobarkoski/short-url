import pytest
import requests

def test_redirection():
    url = 'http://127.0.0.1:8000/RA1UXjh'

    response = requests.get(url)
    if response.status_code == 200:
        assert response.text != None
    else:
        assert False

def test_home_info():
    url = 'http://127.0.0.1:8000/'

    response = requests.get(url)
    if response.status_code == 200:
        assert response.text != None
    else:
        assert False        