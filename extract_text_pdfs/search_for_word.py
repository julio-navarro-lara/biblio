#Copyright 2018 Julio Navarro
#Built at the University of Strasbourg (France). CSTB team @ ICube laboratory
from __future__ import division
from os import path
from glob import glob
import sys


def find_ext(dr, ext):
    return glob(path.join(dr,"*.{}".format(ext)))

def search(text,n):
    '''Searches for text, and retrieves n words either side of the text, which are retuned seperatly'''
    word = r"\W*([\w]+)"
    groups = re.search(r'{}\W*{}{}'.format(word*n,'place',word*n), text).groups()
    return groups[:n],groups[n:]

def main(searched_word):
    list_files = find_ext("output/","txt")
    total_number = len(list_files)
    print "There are "+str(total_number)+" documents"
    result = []
    opposite_result = []

    for filepath in list_files:
        with open(filepath,'rb') as f:
            text = f.read()
            output_name = filepath.rsplit('/',1)[1].split('.',1)[0]
            if searched_word in text:
                result.append(output_name)
            else:
                opposite_result.append(output_name)

    number_found = len(result)
    with open("stats/"+searched_word+".txt","w") as f:
        f.write("Searched word: "+searched_word+"\n")
        f.write("Total number of documents: "+str(total_number)+"\n")
        f.write("Documents where found: "+str(number_found)+"\n")
        f.write("Proportion: "+str(round((number_found/total_number)*100,2))+"%\n")
        f.write("List:\n")
        result.sort()
        for element in result:
            f.write(element+"\n")
        f.write("\nOpposite list (where we do not find the term):\n")
        opposite_result.sort()
        for element in opposite_result:
            f.write(element+"\n")

    print("Searched word: "+searched_word+"\n")
    print("Total number of documents: "+str(total_number)+"\n")
    print("Documents where found: "+str(number_found)+"\n")
    print("Proportion: "+str(round((number_found/total_number)*100,2))+"%\n")



if __name__=="__main__":
    main(sys.argv[1])
