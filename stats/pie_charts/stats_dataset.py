import peewee as pw
import sys
import operator
import itertools

sys.path.insert(0,'../../')

from models import Biblio

selection = Biblio.select(Biblio.dataset).where((Biblio.main_objective.contains('detection'))&(Biblio.julio_state.contains('integrated'))&(Biblio.type_experiment.contains("public")))

equivalence_dict = {
'private_dataset':'NULL',
'darpa_1999':'NULL',
'darpa_2000': 'DARPA 2000',
'simulation': 'NULL',
'nsa_interservice_academy_cyber_defense_competition': 'NSA ...',
'2002_UCSB_treasure_hunt': 'UCSB',
'2004_ucsb_treasure_hunt': 'UCSB',
'darpa_gcp': 'DARPA GCP',
'darpa_gcp_v3_1': 'DARPA GCP',
'darpa_gcp_v3_2': 'DARPA GCP',
'darpa_gcp_v2_0': 'DARPA GCP',
'defcon_2010_18': 'DEFCON',
'2008_ucsb_ictf': 'UCSB',
'defcon_8': 'DEFCON',
'defcon_9': 'DEFCON'
}

list_of_elements = ['DARPA 2000','DARPA GCP','DEFCON','UCSB','NSA ...']

def extract_datasets_occurences():

    result_dict = {}

    for reference in selection:
        splitted_dataset_list = [x.strip() for x in reference.dataset.split(',')]
        for element in splitted_dataset_list:
            if element not in result_dict:
                result_dict[element] = 1
            else:
                result_dict[element] += 1

    return result_dict

def extract_translated_datasets_occurences():
    result_dict = {}

    for reference in selection:
        splitted_dataset_list = [x.strip() for x in reference.dataset.split(',')]
        for element in splitted_dataset_list:
            translated_element = translate_term(element)
            if translated_element != 'NULL':
                if translated_element not in result_dict:
                    result_dict[translated_element] = 1
                else:
                    result_dict[translated_element] += 1

    return result_dict

def translate_term(dataset):
    if dataset in equivalence_dict:
        return equivalence_dict[dataset]
    else:
        print 'There is one not contemplated: '+dataset
        return 'NULL'

def translate_all_elements():
    result_list = []

    for reference in selection:
        splitted_dataset_list = [x.strip() for x in reference.dataset.split(',')]
        subresult_list = []
        for element in splitted_dataset_list:
            translated_element = translate_term(element)
            if translated_element != 'NULL':
                subresult_list.append(translated_element)
        result_list.append(subresult_list)

    return result_list

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

def get_combinations_of_terms_by_2(list_to_search):
    #result = [zip(x,list_of_elements) for x in itertools.permutations(list_of_elements,len(list_of_elements))]
    result = {}
    list_of_pairs = get_only_elements_with_size(2,list_to_search)
    for i in range(0,len(list_of_elements)):
        for j in range(i+1,len(list_of_elements)):
            first_element_to_search = list_of_elements[i]
            second_element_to_search = list_of_elements[j]
            total_number_of_this = 0
            for pair in list_of_pairs:
                if (first_element_to_search in pair) and (second_element_to_search in pair):
                    total_number_of_this += 1

            if total_number_of_this != 0:
                result[first_element_to_search+"; "+second_element_to_search] = total_number_of_this
            #print list_of_elements[i]+' '+list_of_elements[j]
    return result

def get_combinations_of_terms_by_3(list_to_search):
    #result = [zip(x,list_of_elements) for x in itertools.permutations(list_of_elements,len(list_of_elements))]
    result = {}
    list_of_triplets = get_only_elements_with_size(3,list_to_search)
    for i in range(0,len(list_of_elements)):
        for j in range(i+1,len(list_of_elements)):
            for k in range(j+1,len(list_of_elements)):
                first_element_to_search = list_of_elements[i]
                second_element_to_search = list_of_elements[j]
                third_element_to_search = list_of_elements[k]
                total_number_of_this = 0
                for triplet in list_of_triplets:
                    if (first_element_to_search in triplet) and (second_element_to_search in triplet) and (third_element_to_search in triplet):
                        total_number_of_this += 1

                if total_number_of_this != 0:
                    result[first_element_to_search+"; "+second_element_to_search+"; "+third_element_to_search] = total_number_of_this
                #print list_of_elements[i]+' '+list_of_elements[j]
    return result

def get_only_elements_with_size(size, input):
    #We take only those elements whose of an array of arrays whose size is 'size'
    result = []
    for element in input:
        if len(element)==size:
            result.append(element)
        elif len(element) > size:
            print "There are elements with size: "+str(len(element))
            print "It is "
            print element

    return result


def main():
    result_dict = extract_translated_datasets_occurences()
    dict_in_standard_output(result_dict)

    result_dict = get_combinations_of_terms_by_2(translate_all_elements())
    dict_in_standard_output(result_dict)

    result_dict = get_combinations_of_terms_by_3(translate_all_elements())
    dict_in_standard_output(result_dict)
    # result_dictionary = extract_stats_datasets()
    # array = sort_dictionary(result_dictionary)
    # print array
    # array2 = transform_in_percentages(array)
    # print array2
    # represent_pie(array2,"pie_dataset")

if __name__ == "__main__":
    sys.exit(main())
