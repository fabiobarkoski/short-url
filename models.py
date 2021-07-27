from pony.orm import *

db = Database()


class Short(db.Entity):
    '''
    Tabela 'Short' e suas 2 colunas
    '''
    original_link = Required(str)
    short_link = Required(str)


db.bind(provider='postgres', user='', password='', host='', database='')


db.generate_mapping(create_tables=True)
set_sql_debug(True)


@db_session
def save(original_link, short_link):
    '''
    Função para salvar os novos dados inseridos
    '''
    Short(original_link=original_link, short_link=short_link)


@db_session
def search_by_original_link(link):
    '''
    Função de busca de URL original pela URL original
    '''
    s = select(s for s in Short if s.original_link == link)
    for i in s:
        return i.original_link


@db_session
def search_by_short_link(link):
    '''
    Função de busca de URL original pela URL encurtada
    '''
    s = select(s for s in Short if s.short_link == link)
    for i in s:
        return i.original_link


@db_session
def compare_random_letters(random_letters):
    '''
    Função de busca que compara os caracteres aleatórios
    com os caracteres das URL's encurtadas,
    retorna a URL encurtada
    '''
    s = select(s for s in Short if s.short_link == random_letters)
    for i in s:
        return i.short_link
