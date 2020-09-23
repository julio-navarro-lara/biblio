import peewee as pw
import sys

sys.path.insert(0,'../../')

from models import Biblio

dataset_correspondance = {
"defcon_2010_18":"DEFCON ",
"defcon_19":"DEFCON ",
"defcon_8":"DEFCON ",
"defcon_9":"DEFCON ",
"darpa_2000":"DARPA_2000 ",
"2004_ucsb_treasure_hunt":"UCSB ",
"2002_UCSB_treasure_hunt":"UCSB ",
"2008_ucsb_ictf":"UCSB ",
"nsa_interservice_academy_cyber_defense_competition":"NSA ",
"darpa_gcp_v2_0":"DARPA_GCP ",
"darpa_gcp_v3_2":"DARPA_GCP ",
"darpa_gcp_v3_1":"DARPA_GCP ",
"darpa_gcp":"DARPA_GCP ",
"darpa_gcp_4_1":"DARPA_GCP ",
"iscx_unb_ids_dataset":"ISCX "
}

def selector_by_dataset():
    selection = Biblio.select().where(Biblio.julio_state.contains("integrated_core"))
    selection_array = []
    for element in selection:
        string_dataset = element.dataset
        splitted_string = string_dataset.split(',')
        for element2 in splitted_string:
            selection_array.append(change_name(element2))
    return selection_array

def specific_selector_by_dataset():
    selection = Biblio.select().where(Biblio.julio_state.contains("integrated_core"))
    selection_array = []
    for element in selection:
        string_dataset = element.dataset
        splitted_string = string_dataset.split(',')
        result_string = ""
        for element2 in splitted_string:
            result_string += change_name(element2)
        selection_array.append(result_string)
    return selection_array

def change_name(string_to_change):
    if string_to_change in dataset_correspondance:
        return dataset_correspondance[string_to_change]
    else:
        return ""

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

    list_to_search=selector_by_dataset()

    if list_to_search:
        dict_count = extract_repetitions(list_to_search)
        dict_in_standard_output(dict_count)

    print "***************************"

    list_to_search=specific_selector_by_dataset()

    if list_to_search:
        dict_count = extract_repetitions(list_to_search)
        dict_in_standard_output(dict_count)

if __name__ == "__main__":
    sys.exit(main())
