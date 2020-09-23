#Copyright 2018 Julio Navarro
#Built at the University of Strasbourg (France). CSTB team @ ICube laboratory
import peewee as pw
import sys

sys.path.insert(0,'../')

from models import PossibleReferencesC2

def selector_by_coming_from():
    selection_array = []
    selection = PossibleReferencesC2.select(PossibleReferencesC2.coming_from)
    for element in selection:
        selection_array.append(element.coming_from)
    return selection_array

def extract_repetitions(input_list):
    different_elements_set = set(input_list)

    different_elements = list(different_elements_set)

    different_elements.sort()

    dict_count = {}
    for element in different_elements:
        total_number = input_list.count(element)
        dict_count[element] = total_number

    return dict_count

def dict_in_standard_output(dict):
    total = 0

    for key in dict:
        total += dict[key]

    cumulated_percentage = 0

    for key in dict:
        string_to_print = "NULL"
        if key != None:
            string_to_print = key

        quantity = dict[key]
        percentage = round(float(quantity)*100/total,1)
        print string_to_print + '\t' + str(quantity) + '\t' + str(percentage) + '%'
        cumulated_percentage += percentage
    print ""
    print "TOTAL\t" + str(total) + '\t' + str(cumulated_percentage)

def main():
    list_to_search = selector_by_coming_from()

    if list_to_search:
        dict_count = extract_repetitions(list_to_search)
        dict_in_standard_output(dict_count)

if __name__ == "__main__":
    sys.exit(main())
