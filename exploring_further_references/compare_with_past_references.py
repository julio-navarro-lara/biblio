#Copyright 2018 Julio Navarro
#Built at the University of Strasbourg (France). CSTB team @ ICube laboratory
import peewee as pw
import sys
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

sys.path.insert(0,'../')
sys.path.insert(0,'../database_queries/')

from database_queries_reducedreferencesc2 import *
from models import ReducedReferencesC2
from models import Biblio

def compare_with_old_references():

    array_for_comparing = extract_array_for_comparing()

    list_of_references = ReducedReferencesC2.select()

    for element in list_of_references:
        chosen_element = find_maximum_similarity(element.reference,array_for_comparing)

        if chosen_element[2] > 75:
            update_bibtex_id(element.id,chosen_element[1])
            update_reference_string(element.id,chosen_element[0])

def extract_array_for_comparing():
    selection = Biblio.select()
    result = []

    for element in selection:
        result.append([element.plain_text_reference,element.bibtex_id])

    return result

def find_maximum_similarity(reference_string,array_for_comparing):
    #It returns a triplet: (reference_string, bibtex_id, similarity)
    chosen_element = ["","",0]
    for element in array_for_comparing:
        similarity = fuzz.token_set_ratio(element[0],reference_string)
        if similarity > chosen_element[2]:
            chosen_element = [element[0],element[1],similarity]
    return chosen_element

def main():
    compare_with_old_references()

if __name__ == "__main__":
    sys.exit(main())
