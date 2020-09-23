#Copyright 2018 Julio Navarro
#Built at the University of Strasbourg (France). CSTB team @ ICube laboratory
import peewee as pw
import sys

sys.path.insert(0,'../')
sys.path.insert(0,'../database_queries/')

from database_queries_biblio import *
from models import Biblio

selection = Biblio.select()

def extract_plain_reference_through_references():
    for element in selection:
        author = "NULL"
        title ="NULL"
        journal ="NULL"
        publisher ="NULL"
        volume ="NULL"
        issue ="NULL"
        pages ="NULL"
        if element.author:
            author = element.author
        if element.title:
            title = element.title
        if element.journal:
            journal = element.journal
        if element.publisher:
            publisher = element.publisher
        if element.volume:
            volume = element.volume
        if element.issue:
            issue = element.issue
        if element.pages:
            pages = element.pages

        plain_text_reference = compose_plain_text_reference(
            author,
            title,
            journal,
            publisher,
            volume,
            issue,
            pages,
            str(element.year))

        update_plain_text_reference(element.bibtex_id,plain_text_reference)

def compose_plain_text_reference(author,title,journal,publisher,volume,issue,pages,year):
    result = ""
    if author != "NULL":
        result += author
    if title != "NULL":
        result += ", "+title
    if journal != "NULL":
        result += ", "+journal
    if publisher != "NULL":
        result += ", "+publisher
    if volume != "NULL":
        result += ", "+volume
    if issue != "NULL":
        result += ", "+issue
    if pages != "NULL":
        result += ", "+pages
    if year != "NULL":
        result += ", "+year
    return result

def main():
    extract_plain_reference_through_references()

if __name__ == "__main__":
    sys.exit(main())
