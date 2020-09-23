#Copyright 2018 Julio Navarro
#Built at the University of Strasbourg (France). CSTB team @ ICube laboratory
import sys
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def read_file(fname):
    with open(fname) as f:
        content = f.read()
    return content

def split_content_by_semicolon(input):
    return input.split(';')

def cross_comparison(result_array1, result_array2):
    #Cross comparison
    result_cross_comparison = []
    for element1 in result_array1:
        partial_array = []
        for element2 in result_array2:
            partial_array.append(fuzz.token_set_ratio(element1,element2))
        result_cross_comparison.append(partial_array)
    return result_cross_comparison

def same_comparison(result_array1):
    #Same comparison
    result_same_comparison = []
    for element1 in result_array1:
        partial_array = []
        #We erase the element that is the same, of course
        erased_result_array1 = result_array1.remove(element1)
        for element2 in result_array1:
            partial_array.append(fuzz.token_set_ratio(element1,element2))
        result_same_comparison.append(partial_array)
    return result_same_comparison

def stats_by_row(input_2D_list):
    counter = 0
    for list in input_2D_list:
        print "Stats element- "+str(counter)+extract_stats(list)
        counter += 1

def extract_stats(input_array):

    return "\taverage: "+str(mean(input_array))+"\tmax: "+str(max(input_array))+"\tmin: "+str(min(input_array))

def unify_2d_list(input_2D_list):
    result = []
    for list in input_2D_list:
        for element in list:
            result.append(element)
    return result

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

def print_array(input_array):
    for element in input_array:
        print element

def print_stats(result_cross_comparison,result_same_comparison):
    #Stats by element
    print "****************"
    print "CROSS COMPARISON"
    stats_by_row(result_cross_comparison)
    print "****************"
    print "SAME COMPARISON"
    stats_by_row(result_same_comparison)

    #Global stats
    print "****************"
    print "GLOBAL STATS"
    print "Cross comparison: "+extract_stats(unify_2d_list(result_cross_comparison))
    print "Same comparsion: "+extract_stats(unify_2d_list(result_same_comparison))

def main():
    fname = "test_techniques_and_tools.txt"
    result_array1 = split_content_by_semicolon(read_file(fname))
    fname = "test_julisch.txt"
    result_array2 = split_content_by_semicolon(read_file(fname))

    #Cross comparison
    result_cross_comparison = cross_comparison(result_array1,result_array2)

    #Same comparison
    result_same_comparison = same_comparison(result_array1)

    print_stats(result_cross_comparison,result_same_comparison)
    #print_array(result_array1)




if __name__ == "__main__":
    sys.exit(main())
