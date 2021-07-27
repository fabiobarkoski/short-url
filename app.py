import os
from sanic import Sanic
from sanic.views import HTTPMethodView
from sanic.response import json, redirect, html
from models import *
import string
import random

app = Sanic('app')


def generator():
    '''
    Função que gera aleatóriamente números
    e letras a serem utilizadas na criação da URL
    '''
    size = 7
    w = string.ascii_letters + string.digits
    return ''.join(random.choice(w) for i in range(size))


class home(HTTPMethodView):
    '''
    Classe que é a 'view index' da API
    '''
    async def get(self, request):
        '''
        HTML simples de bem-vindo
        '''
        return html('''<!DOCTYPE html>
                       <html lang="en">
                       <meta charset="UTF-8">
                       <div>
                       <h1>Welcome to the URL Shortner API</h1>
                       </div>''')

    async def post(self, request):
        '''
        Função de cadastro das URL's
        '''
        data = request.json
        short_link = generator()
        if search_by_original_link(data['link']) == data['link']:

            return json({'status': 200,
                         'message': 'este link ja esta encurtado '})
        else:
            while short_link == compare_random_letters(short_link):
                short_link = generator()
            try:
                save(data['link'], short_link)
            except:
                print('ERROR')

            return json({'status_code': 200,
                         'status': 'success',
                         'Link': 'your.domain/'+short_link})


@app.get('/<link:str>')
async def redirect_to(request, link):
    '''
    Função que pega o a URL encurtada e redireciona
    para a URL original
    '''
    url = app.url_for('redirect_view', _external=True,
                      _server=search_by_short_link(link))
    return redirect(url)


@app.head('')
async def redirect_view(request):
    '''
    Função base necessária para o redirecionamento
    '''
    pass

app.add_route(home.as_view(), '/')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
