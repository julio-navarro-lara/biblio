import peewee as pw
import operator
import sys

sys.path.insert(0,'../../')

from models import Biblio
from representation_pie import *



selection = Biblio.select(Biblio.type_data).where((Biblio.main_objective=='detection')&(Biblio.julio_state.contains("integrated")))

def count_distict_data():
    result_dictionary = {}

    for element in selection:
        if element.type_data:
            if element.type_data in result_dictionary:
                result_dictionary[element.type_data] += 1
            else:
                result_dictionary[element.type_data] = 1

    return result_dictionary

def transform_in_percentages(array_tuple):
    sum = 0
    for element in array_tuple:
        sum += element[1]

    #First the item and them the percentage *100
    result_array_tuple = []
    for element in array_tuple:
        result_array_tuple.append([element[0], int(round((float(element[1])/float(sum))*100))])

    return result_array_tuple

def sort_dictionary(entry_dictionary):
    #it sorts a dictionary by value in the reverse mode and returns an array of tuples, with the first element the key and the second the value
    return sorted(entry_dictionary.items(), key=operator.itemgetter(1), reverse=True)

def main():
    result_dictionary = count_distict_data()
    array = sort_dictionary(result_dictionary)
    print array
    array2 = transform_in_percentages(array)
    print array2
    represent_pie(array2,"pie_type_data")

if __name__ == "__main__":
    sys.exit(main())
