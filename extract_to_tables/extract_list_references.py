#Copyright 2018 Julio Navarro
#Built at the University of Strasbourg (France). CSTB team @ ICube laboratory
import peewee as pw
import sys

sys.path.insert(0,'../')
sys.path.insert(0,'../database_queries/')

from database_queries_possiblereferencesc2 import *
from models import PossibleReferencesC2
from models import Biblio

def create_table():
    try:
        PossibleReferencesC2.create_table()
    except pw.OperationalError:
        print "Table already exists!"

def extract_list_of_references(julio_state):
    selection = Biblio.select().where(Biblio.julio_state.contains(julio_state))
    counter = 1

    for element in selection:
        list_of_references = element.raw_bibliography.split(';')
        for reference in list_of_references:
            new_entry({"id":counter,"reference":reference,"coming_from":element.bibtex_id})
            counter += 1

def main():
    create_table()
    extract_list_of_references(sys.argv[1])

if __name__ == "__main__":
    sys.exit(main())
