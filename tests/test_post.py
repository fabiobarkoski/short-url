import pytest
import requests
import json


def test_data_insert():
    '''
    Função que testa a inserção de dados da API
    '''
    url = 'http://127.0.0.1:8000/'

    new_link = {'link': 'test.com'}

    response = requests.post(url, data=json.dumps(new_link))
    response_dict = response.json()

    if response.status_code == 200:
        status = response_dict['status']
        short_link = response_dict['Link']

        assert status == 'success' and short_link is not None
    else:
        assert False
