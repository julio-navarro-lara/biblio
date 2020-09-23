#Copyright 2018 Julio Navarro
#Built at the University of Strasbourg (France). CSTB team @ ICube laboratory
from refextract import extract_references_from_file
from refextract import extract_references_from_string
from pathlib2 import Path

import re
import sys

sys.path.insert(0,'../')
sys.path.insert(0,'../database_queries/')

from models import Biblio
from database_queries_biblio import *

def array_to_semicolon_separated(input):
    result = input[0]

    for element in input[1:]:
        result += ";"
        result += element

    return result

def extract_citations_from_pdf(name_of_file):
    references = extract_references_from_file(name_of_file)
    #reference = extract_references_from_string("text.txt")

    print "**************"

    array_of_citations = []

    for element in references:
        for key in element:
            print key
            print element[key]
            print "---"

        #array_of_citations.append(element['raw_ref'][0].replace(u'['+element['linemarker'][0]+u'] ',u''))
        array_of_citations.append(element['raw_ref'][0])
        print "**************"

    if len(array_of_citations)>1:
        string_of_citations = array_to_semicolon_separated(array_of_citations)
    elif len(array_of_citations)==1:
        string_of_citations = array_of_citations[0]
    else:
        string_of_citations = "No references to extract"

    print string_of_citations
    return string_of_citations
#Puede haber pdfs en los que las referencias esten mal. Hay que revisar
#Esto solo detecta en funcion de los numeros entre corchetes, y sigue la numeracion
#Comprobar que no haya corchetes mas alla del inicio en la referencia

def extract_citations_in_database():
    selection = Biblio.select(Biblio.bibtex_id).where(Biblio.raw_bibliography.is_null())

    global_path = "/Users/Julio/Documents/PhD/Papers/Security/Multi-Step attacks DB/"

    for element in selection:
        try:
            string_of_path = global_path+"Corpus/"+element.bibtex_id+".pdf"
            path_to_file = Path(string_of_path)
            if not path_to_file.is_file():
                string_of_path = global_path+"Papers/"+element.bibtex_id+".pdf"
                path_to_file = Path(string_of_path)
                if path_to_file.is_file():
                    string_with_references = extract_citations_from_pdf(string_of_path)
                else:
                    print "NOT WORKED"
                    string_with_references = "NOT WORKED"
            else:
                string_with_references = extract_citations_from_pdf(string_of_path)

            update_raw_bibliography(element.bibtex_id,string_with_references)
        except TypeError,IndexError:
            print "Not worked for: "+element.bibtex_id
            update_raw_bibliography(element.bibtex_id,"SOME ERROR OF THE PROGRAM")

def main():
    #extract_citations_from_pdf("test.pdf")
    extract_citations_in_database()

if __name__ == "__main__":
    sys.exit(main())
