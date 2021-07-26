import random
from pony.orm import *

db = Database()

class Short(db.Entity):
    original_link = Required(str)
    short_link = Required(str)

db.bind(provider='postgres', user='bzclzhideovtes', password='ef5e43b3e89d0bf8871d841a86be6b8bcf63b86f4e47bd3a31f444f15106d851', host='ec2-23-21-4-7.compute-1.amazonaws.com', database='df26bllk2v7ho6')


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