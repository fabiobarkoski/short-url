from sanic import Sanic
from sanic.response import  json, redirect
from models import save, search_by_original_link, search_by_short_link
import string, random

app = Sanic('app')

def generator():
    size = 7
    w = string.ascii_letters + string.digits
    return ''.join(random.choice(w) for i in range(size))

@app.post('/')
async def add(request):
    data = request.json
    short_link = 'your.domain/'+generator()
    if search_by_original_link(data['link']) == data['link']:
        return json({'status' : 200,
                    'message' : 'este link ja esta encurtado '})
    else:
        try:
            save(data['link'], short_link)
            print('CADASTRADO COM SUCESSO!')
        except:
            print('ERROR')
        return json({'status' : 200,
                    'New Link' : short_link})

@app.get('/<link:str>/')
async def redirect_to(request, link):
    url = app.url_for('redirect_view', _external=True, _server=search_by_short_link(link))
    return redirect(url)

@app.route('')
async def redirect_view(request):
    pass


if __name__ == '__main__':
    app.run(debug=True)
    