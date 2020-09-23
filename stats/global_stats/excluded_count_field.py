import peewee as pw
import sys

sys.path.insert(0,'../../')

from models import Excluded_phase_b

def selector(input):

    selection_array=[]

    if input=="reason":
        selection_array = selector_by_reason()
    else:
        print "The field \""+input+"\" is not a valid field in the database"

    return selection_array

def selector_by_reason():
    selection = Excluded_phase_b.select(Excluded_phase_b.reason)
    selection_array = []
    if selection != None:
        for element in selection:
            selection_array.append(element.reason)
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

    total_perc = 0
    for key in dict:
        if key != None:
            print key + '\t'
            print str(dict[key]) + '\t' + str(round((float(dict[key])/float(total))*100,1)) + "%"
        else:
            print "NULL\t"
            print str(dict[key]) + '\t' + str(round((float(dict[key])/float(total))*100,1)) + "%"

        total_perc += round((float(dict[key])/float(total))*100,1)

    print ""
    print "TOTAL\t" + str(total)
    print "Total perc\t" + str(total_perc) + "%"

def extract_count_as_dict(fieldname):
    list_to_search = selector(fieldname)
    if list_to_search:
        dict_count = extract_repetitions(list_to_search)

    return dict_count

def main():
    if len(sys.argv) == 1:
        list_to_search = None
        print "There is no argument"
    elif len(sys.argv) == 2:
        list_to_search = selector(sys.argv[1])

    if list_to_search:
        dict_count = extract_repetitions(list_to_search)
        dict_in_standard_output(dict_count)

if __name__ == "__main__":
    sys.exit(main())
