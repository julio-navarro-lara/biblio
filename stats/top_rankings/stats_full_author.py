import peewee as pw
import sys
import operator
import re
from representation_ranking import represent_ranking_in_table

sys.path.insert(0,'../../')

from models import Biblio

selection = Biblio.select(Biblio.full_author, Biblio.bibtex_id).where((Biblio.main_objective == 'detection')&(Biblio.julio_state.contains("integrated")))

def extract_authors():
    names = []
    for reference in selection:
        names = names + [x.strip() for x in reference.full_author.split(' and ')]

    different_names_set = set(names)

    different_names = list(different_names_set)

    different_names.sort()
    counter_others = 0

    dictionary_of_names = {}

    for element in different_names:
        total_number = names.count(element)
        dictionary_of_names[element] = total_number
        print element + '\t' + str(total_number)

    return sort_dictionary(dictionary_of_names)

def sort_dictionary(entry_dictionary):
    #it sorts a dictionary by value in the reverse mode and returns an array of tuples, with the first element the key and the second the value
    return sorted(entry_dictionary.items(), key=operator.itemgetter(1), reverse=True)

def select_top(array_to_select,number_of_items):
    return array_to_select[0:number_of_items]

def make_array_richer(array):
    result = []
    for element in array:
        all_papers = Biblio.select().where((Biblio.main_objective.contains('detection'))&(Biblio.full_author.contains(element[0]))&(Biblio.julio_state.contains("integrated"))).count()
        print str(all_papers) + " ==== " + str(element[1])

    return result

def main():
    number_of_items = 10
    array_to_represent = select_top(extract_authors(),number_of_items)
    make_array_richer(array_to_represent)
    represent_ranking_in_table(array_to_represent,number_of_items,'ranking_authors.tex','Ranking of top '+str(number_of_items)+' authors according to the number of papers included in the review')

if __name__ == "__main__":
    sys.exit(main())
