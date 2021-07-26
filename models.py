from pony.orm import *

db = Database()

class Short(db.Entity):
    original_link = Required(str)
    short_link = Required(str)

db.bind(provider='postgres', user='pfmehycgspdebl', password='fbb11ba8ac40cb21bf77b4c789a589cb62dec4c0062576bf4e25edf62e4871f9', host='ec2-52-72-125-94.compute-1.amazonaws.com', database='d64j28tkduodc2')


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
    s = select(s for s in Short if s.short_link == link)
    for i in s:
        return i.original_link

@db_session
def compare_random_letters(random_letters):
    s = select(s for s in Short if s.short_link == random_letters)
    for i in s:
        return i.short_link