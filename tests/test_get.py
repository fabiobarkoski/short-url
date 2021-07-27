import pytest
import requests


def test_redirection():
    '''
    Função que testa o redirecionamento da API
    '''
    url = 'http://127.0.0.1:8000/RA1UXjh'

    response = requests.get(url)
    if response.status_code == 200:
        assert response.text is not None
    else:
        assert False


def test_home_info():
    '''
    Função que testa o acesso ao bem-vindo da API
    '''
    url = 'http://127.0.0.1:8000/'

    response = requests.get(url)
    if response.status_code == 200:
        assert response.text is not None
    else:
        assert False
