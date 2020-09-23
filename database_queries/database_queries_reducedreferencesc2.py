#Copyright 2018 Julio Navarro
#Built at the University of Strasbourg (France). CSTB team @ ICube laboratory
import peewee as pw
import sys
import string
import unidecode

sys.path.insert(0,'../')

from models import ReducedReferencesC2

def new_entry(dict_entry):
    ReducedReferencesC2.create(id=dict_entry["id"],
    reference=dict_entry["reference"].encode('utf-8'),
    coming_from=dict_entry["coming_from"])

    return True

# def update_references(new_reference, new_coming_from, id_ref):
#     ref = ReducedReferencesC2.get(ReducedReferencesC2.id == id_ref)
#     query = ReducedReferencesC2.update(reference=ref.reference+";"+new_reference).where(PossibleReferencesC2.id == id_ref)
#     query.execute()
#     query = ReducedReferencesC2.update(coming_from=ref.coming_from+";"+new_coming_from).where(PossibleReferencesC2.id == id_ref)
#     query.execute()

def update_bibtex_id(id_ref, new_bibtex_id):
    query = ReducedReferencesC2.update(bibtex_id=new_bibtex_id).where(ReducedReferencesC2.id == id_ref)
    query.execute()

def update_reference_string(id_ref, new_value):
    query = ReducedReferencesC2.update(reference_string=new_value.encode('utf-8')).where(ReducedReferencesC2.id == id_ref)
    query.execute()

def main():
    print "test"
    #update_citations_google('99_Huang',10000)
    #update_url('99_Huang', 'cualquier cosa')
    #update_url_pdf('99_Huang', 'cualquier cosa')
    #update_clusterid_google('99_Huang', 'cualquier cosa')

if __name__ == "__main__":
    sys.exit(main())
