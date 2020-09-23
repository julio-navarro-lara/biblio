import peewee as pw
import sys

sys.path.insert(0,'../../')

from models import Biblio
from representation_graphs import *

def extract_number_of_papers_per_approach(approaches, begin_year, end_year):
    #It accept an array of duples called "type" with the "key" the type to print and in the value an array of the values to search
    #We are going to use the same structure of types but we are going to change the arrays of subtypes by the data extracted from the dataset for doing the plots
    result = approaches
    paper_counter = 0
    counter = 0
    for global_tuple in approaches:
        #The global types they are already in "result"
        plot_for_type = []
        for i in range(begin_year,end_year):
            #We need to look for all the entries having the subtypes as types and we count the result
            number_of_results = 0
            for subtype in global_tuple[1]:
                number_of_results += Biblio.select().where((Biblio.year==i) & (Biblio.approach==subtype) & (Biblio.julio_state.contains("integrated_core")) & (Biblio.main_objective.contains("detection"))).count()

            plot_for_type.append([i,number_of_results])
            paper_counter += number_of_results

        result[counter][1] = plot_for_type
        counter += 1



    print "Total number of papers extracted: "+str(paper_counter)
    return result

def get_approaches_according_to_paper():
    #It returns the type of papers hard-coded in this code.
    #It returns an array of arrays. In each subarray you have all the types corresponding to the general type in the "key"
    return [["Similarity-based",["similarity_progressive_construction","similarity_scenario_clustering","similarity_anomaly_detection"]],
    ["Causal correlation",["sequence_causal_correlation","sequence_probability_analysis"]],
    ["Case-based",["case_centralized","case_distributed"]],
    ["Mixed",["mixed"]],
    ["Structural-based",["structural_projection"]]
    ]

def output_console_results(result_array):
    for group_element in result_array:
        print group_element[0] + " : "
        for element in group_element[1]:
            print str(element[0]) + " : " + str(element[1])

    for group_element in result_array:
        print group_element[0] + " : "
        result_string = ""
        for element in group_element[1]:
            result_string += "("+str(element[0])+","+str(element[1])+") "
        print result_string

def main():
    result = extract_number_of_papers_per_approach(get_approaches_according_to_paper(),2001,2019)
    represent_separated_histogram(result,"papers_per_year_histogram_v2")

    output_console_results(result)

if __name__ == "__main__":
    sys.exit(main())
