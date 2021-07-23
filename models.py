from pony.orm import *

db = Database()

class Short(db.Entity):
    original_link = Required(str)
    short_link = Required(str)

db.bind(provider='', user='', password='', host='', database='')


db.generate_mapping(create_tables=True)
set_sql_debug(True)

@db_session
def save(original_link, short_link):
    Short(original_link=original_link, short_link=short_link)

@db_session
def search_by_original_link(link):
    s = select(s for s in Short if s.original_link == link)
    for i in s:
        return i.original_link

@db_session
def search_by_short_link(link):
    short_link = 'your.domain/' + link
    s = select(s for s in Short if s.original_link == short_link)
    for i in s:
        return i.original_link