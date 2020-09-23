#Copyright 2018 Julio Navarro
#Built at the University of Strasbourg (France). CSTB team @ ICube laboratory
import peewee as pw
import sys
import string
import unidecode

sys.path.insert(0,'../')

from models import OrderedReferencesC2

def new_entry(dict_entry):
    OrderedReferencesC2.create(id=dict_entry["id"],
    reference=dict_entry["reference"].encode('utf-8'),
    coming_from=dict_entry["coming_from"])

    return True

def main():
    print "test"
    #update_citations_google('99_Huang',10000)
    #update_url('99_Huang', 'cualquier cosa')
    #update_url_pdf('99_Huang', 'cualquier cosa')
    #update_clusterid_google('99_Huang', 'cualquier cosa')

if __name__ == "__main__":
    sys.exit(main())
