#Copyright 2018 Julio Navarro
#Built at the University of Strasbourg (France). CSTB team @ ICube laboratory
import peewee as pw
import sys
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

sys.path.insert(0,'../')
sys.path.insert(0,'../database_queries/')

from database_queries_orderedreferencesc2 import *
from models import PossibleReferencesC2
from models import ReducedReferencesC2
from models import OrderedReferencesC2

def create_table():
    try:
        OrderedReferencesC2.create_table()
    except pw.OperationalError:
        print "Table already exists!"

def extract_possible_references():
    selection = PossibleReferencesC2.select()

    result = []
    #We save first all the elements in a list of duples [reference,coming_from]
    for element in selection:
        result.append([element.reference,element.coming_from])

    return result

def merge_references(list_of_references):
    result = []
    counter = 1

    comparison_list = []

    for element1 in list_of_references:

        create_new = True
        for element2 in result:
            comparison = fuzz.token_set_ratio(element1[0],element2["first_reference"])
            comparison_list.append(comparison)
            if comparison>65:
                #We append a new case of this reference
                element2["references"] += ";"+element1[0]
                element2["coming_from"] += ";"+element1[1]
                create_new = False
            break

        #If there is no match, we create a new reference
        if create_new:
            result.append({
                "id":counter,
                "first_reference":element1[0],
                "references":element1[0],
                "coming_from":element1[1]
            })
            counter += 1

    print max(comparison_list)
    return result

def order_references_by_similarity(list_of_references):

    #first_couple = find_maximum_similarity(list_of_references)
    first_couple = [
        [u"[6] H. Debar and A. Wespi. \u201cThe IntrusionDetection Console Correlation Mechanism\u201d. Workshop on the Recent Advances in Intrusion Detection (RAID\u20192001), Davis, USA, October 2001.",
        u'02_Cuppens'],
        [u'6. Debar, H. and Wespi, A.: The Intrusion Detection Console Correlation Mechanism. Workshop on the Recent Advances in Intrusion Detection (RAID\u20192001), Davis, USA (October 2001)',
        u'03_Benferhat']
    ]

    result_list = [first_couple[0],first_couple[1]]

    print len(list_of_references)

    print result_list[0]
    print result_list[1]

    is_erased_1 = False
    is_erased_2 = False
    for element in list_of_references:
        if (not is_erased_1) & (element[0]==result_list[0][0]):
            list_of_references.remove(element)
            is_erased_1 = True
        elif (not is_erased_2) & (element[0]==result_list[1][0]):
            list_of_references.remove(element)
            is_erased_2 = True
        if is_erased_1 & is_erased_2:
            break

    print len(list_of_references)

    while list_of_references:
        reference_element = result_list[:-1]
        maximum_comparison = 0
        best_match = []
        for element in list_of_references:
            comparison = fuzz.token_set_ratio(reference_element[0],element[0])
            if comparison > maximum_comparison:
                maximum_comparison = comparison
                best_match = element

        print best_match

        result_list.append(best_match)
        list_of_references.remove(best_match)

    return result_list


def find_maximum_similarity(list_of_references):

    max_similarity = 0
    candidate_couple = []
    for i in range(0,len(list_of_references)):

        for j in range(i+1,len(list_of_references)):
            print "i: "+str(i)+"j: "+str(j)
            comparison = fuzz.token_set_ratio(list_of_references[i][0],list_of_references[j][0])
            if comparison > max_similarity:
                max_similarity = comparison
                candidate_couple = [list_of_references[i],list_of_references[j]]


    return candidate_couple


def print_dictionary(merged_result):
    for element in merged_result:
        print str(element["id"])+"\t"+element["references"]+"\t"+element["coming_from"]
        print "************"

def add_list_to_table(result_list):
    counter = 1
    for element in result_list:
        new_entry({"id":counter,
            "reference":element[0],
            "coming_from":element[1]})
        counter+=1

def main():
    #create_table()
    list_of_references = extract_possible_references()
    #merged_result = merge_references(list_of_references)
    #print_dictionary(merged_result)
    #print "NUMBER OF REFERENCES: "+str(len(merged_result))
    #print "NUMBER ORIGINAL REFERENCES: "+str(len(list_of_references))
    result_list = order_references_by_similarity(list_of_references)
    create_table()

    add_list_to_table(result_list)



if __name__ == "__main__":
    sys.exit(main())
