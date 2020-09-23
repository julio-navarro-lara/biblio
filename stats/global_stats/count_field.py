import peewee as pw
import sys

sys.path.insert(0,'../../')

from models import Biblio

def selector(input,objective,state):

    selection_array=[]

    selection= return_selection(objective,state)

    if selection != None:
        if input=="origin":
            selection_array = selector_by_origin(selection)
        elif input=="julio_state":
            selection_array = selector_by_julio_state(selection)
        elif input=="approach":
            selection_array = selector_by_approach(selection)
        elif input=="type_data":
            selection_array = selector_by_type_data(selection)
        elif input=="type_experiment":
            selection_array = selector_by_type_experiment(selection)
        elif input=="dataset":
            selection_array = selector_by_dataset(selection)
        elif input=="knowledge_extraction":
            selection_array = selector_by_knowledge_extraction(selection)
        elif input=="reproducible_method":
            selection_array = selector_by_reproducible_method(selection)
        elif input=="reproducible_experiments":
            selection_array = selector_by_reproducible_experiments(selection)
        elif input=="attack_model":
            selection_array = selector_by_attack_model(selection)
        elif input=="general_approach":
            selection_array = selector_by_general_approach(selection)
        elif input=="group":
            selection_array = selector_by_group(selection)
        else:
            print "The field \""+input+"\" is not a valid field in the database"

    return selection_array

def return_selection(objective,state):
    if objective:
        if state:
            selection = Biblio.select().where((Biblio.main_objective.contains(objective))&(Biblio.julio_state.contains(state)))
        else:
            selection = Biblio.select().where(Biblio.main_objective.contains(objective))
    else:
        selection = Biblio.select()

    return selection

def selector_by_origin(selection):
    selection_array = []
    for element in selection:
        selection_array.append(element.origin)
    return selection_array

def selector_by_julio_state(selection):
    selection_array = []
    for element in selection:
        selection_array.append(element.julio_state)
    return selection_array

def selector_by_approach(selection):
    selection_array = []
    for element in selection:
        selection_array.append(element.approach)
    return selection_array

def selector_by_type_data(selection):
    selection_array = []
    for element in selection:
        selection_array.append(element.type_data)
    return selection_array

def selector_by_type_experiment(selection):
    selection_array = []
    for element in selection:
        selection_array.append(element.type_experiment)
    return selection_array

def selector_by_dataset(selection):
    selection_array = []
    for element in selection:
        selection_array.append(element.dataset)
    return selection_array

def selector_by_knowledge_extraction(selection):
    selection_array = []
    for element in selection:
        selection_array.append(element.knowledge_extraction)
    return selection_array

def selector_by_reproducible_method(selection):
    selection_array = []
    for element in selection:
        selection_array.append(element.reproducible_method)
    return selection_array

def selector_by_reproducible_experiments(selection):
    selection_array = []
    for element in selection:
        selection_array.append(element.reproducible_experiments)
    return selection_array

def selector_by_attack_model(selection):
    selection_array = []
    for element in selection:
        selection_array.append(element.attack_model)
    return selection_array

def selector_by_general_approach(selection):
    selection_array = []
    for element in selection:
        selection_array.append(element.general_approach)
    return selection_array

def selector_by_group(selection):
    selection_array = []
    for element in selection:
        selection_array.append(element.group)
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
    number_of_values = 0

    sum_average = 0
    only_one_occurrence = 0
    only_two_occurrences = 0

    for key in dict:
        string_to_print = "NULL"
        if key != None:
            string_to_print = key

        quantity = dict[key]
        percentage = round(float(quantity)*100/total,1)
        print string_to_print + '\t' + str(quantity) + '\t' + str(percentage) + '%'
        cumulated_percentage += percentage
        number_of_values+=1
        sum_average+=quantity
        if quantity==1:
            only_one_occurrence+=1
        elif quantity == 2:
            only_two_occurrences+=1
    print ""
    print "TOTAL\t" + str(total) + '\t' + str(cumulated_percentage)
    print "Total number of different values\t"+str(number_of_values)
    print "Average number of occurrences\t"+str(float(sum_average)/number_of_values)
    print "Proportion of values with only 1 occurrence\t"+str(only_one_occurrence) + '\t' +str(round(float(only_one_occurrence)*100/number_of_values,1))
    print "Proportion of values with 2 occurrences\t"+str(only_two_occurrences) + '\t' +str(round(float(only_two_occurrences)*100/number_of_values,1))


def extract_count_as_dict(fieldname):
    list_to_search = selector(fieldname)
    if list_to_search:
        dict_count = extract_repetitions(list_to_search)

    return dict_count

def main():
    #First argument in the Python script is the field to count
    #Second argument serve to select "detection" if we want to select only the references in detection
    #Third argument serve to select some string in the column julio_state
    #NOT IMPLEMENTED Forth argument serve to select an element in the column type_experiment
    if len(sys.argv) == 1:
        list_to_search = None
        print "There is no argument"
    elif len(sys.argv) == 2:
        list_to_search = selector(sys.argv[1],"","")
    elif len(sys.argv) == 3:
        list_to_search = selector(sys.argv[1],sys.argv[2],"")
    elif len(sys.argv) == 4:
        list_to_search = selector(sys.argv[1],sys.argv[2],sys.argv[3])

    if list_to_search:
        dict_count = extract_repetitions(list_to_search)
        dict_in_standard_output(dict_count)

if __name__ == "__main__":
    sys.exit(main())
