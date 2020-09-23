#Copyright 2018 Julio Navarro
#Built at the University of Strasbourg (France). CSTB team @ ICube laboratory
# -*- coding: utf-8 -*-
import sys

sys.path.insert(0,'../')
sys.path.insert(0,'../database_queries/')

from database_queries_biblio import *
import bibtexparser
import codecs
import unidecode



def recover_accents_string(entry):
    to_convert = entry.decode("utf-8")

    to_convert.replace("{\\'a}", u"\uc3a1")
    to_convert.replace("{\\'e}", u"\uc3a9")
    to_convert.replace("{\\'i}", u"\uc3ad")
    to_convert.replace("{\\'o}", u"\uc3b3")
    to_convert.replace("{\\'u}", u"\uc3ba")

    to_convert = to_convert.encode("utf-8")

    return to_convert

def import_bibtex_file(filename):
    with codecs.open(filename,'r',encoding='utf8') as bibtex_file:
    #with open(filename) as bibtex_file:
        bibtex_str = bibtex_file.read()
        print bibtex_str
    bib_database = bibtexparser.loads(bibtex_str)
    print(bib_database.entries)
    return bib_database

def translate_entry_type(type):
    if type == "inproceedings":
        result = "Conference Proceedings"
    elif type == "article":
        result = "Journal Article"
    elif type == "phdthesis":
        result = "Thesis"
    elif type == "techreport":
        result = "Report"
    elif type == "inbook":
        result = "Book Section"
    elif type == "book":
        result = "Book"
    else:
        result = "ERROR"

    return result

def compose_bibtex_id(full_author, year):
    two_digit_year = str(year)[-2:]
    authors_in_element = [x.strip() for x in full_author.split(' and ')]
    first_author_separated = [x.strip() for x in authors_in_element[0].split(',')]
    return two_digit_year + "_" + unidecode.unidecode(first_author_separated[0].replace(" ",""))

def decide_id(max_id):
    selection = Biblio.select(Biblio.id)
    #max_id = 0
    for element in selection:
        if element.id > max_id:
            max_id = element.id
    if(max_id < 3000):
        max_id = 3000

    return max_id + 1

def compress_authors(full_author):
    authors_in_element = [x.strip() for x in full_author.split(' and ')]

    number_of_authors = len(authors_in_element)

    counter = 1
    new_string_of_authors = ""

    for author in authors_in_element:
        new_author=""
        split_author = [x.strip() for x in author.split(',')]
        split_first_name = [x.strip() for x in split_author[1].split(' ')]

        for subname in split_first_name:
            new_author = new_author + subname[0] + ". "

        new_author = new_author + split_author[0]

        if counter < number_of_authors:
            new_author += ", "

        if counter==number_of_authors-1 and number_of_authors>1:
            new_author = new_author + "and "

        counter +=1

        new_string_of_authors = new_string_of_authors + new_author

    return new_string_of_authors

def bibtex_dict_to_sql_dict(bibtex_dict, int_id):
    sql_dict = {"id": int_id}
    sql_dict["type"]=translate_entry_type(bibtex_dict["ENTRYTYPE"])

    if "author" in bibtex_dict:
        sql_dict["full_author"] = recover_accents_string(bibtex_dict["author"])
        #sql_dict["author"] = compress_authors(recover_accents_string(bibtex_dict["author"]))
    else:
        print "Error in author in "
        print bibtex_dict

    if "year" in bibtex_dict:
        sql_dict["year"] = int(bibtex_dict["year"])

    if "title" in bibtex_dict:
        sql_dict["title"] = recover_accents_string(bibtex_dict["title"])

    if "journal" in bibtex_dict:
        sql_dict["journal"] = recover_accents_string(bibtex_dict["journal"])
    elif "booktitle" in bibtex_dict:
        sql_dict["journal"] = recover_accents_string(bibtex_dict["booktitle"])

    if "publisher" in bibtex_dict:
        sql_dict["publisher"] = recover_accents_string(bibtex_dict["publisher"])
    elif "school" in bibtex_dict:
        sql_dict["publisher"] = recover_accents_string(bibtex_dict["school"])
    elif "institution" in bibtex_dict:
        sql_dict["publisher"] = recover_accents_string(bibtex_dict["institution"])

    if "volume" in bibtex_dict:
        sql_dict["volume"] = bibtex_dict["volume"]

    if "issue" in bibtex_dict:
        sql_dict["issue"] = bibtex_dict["issue"]

    if "pages" in bibtex_dict:
        sql_dict["pages"] = bibtex_dict["pages"]

    if "ISSN" in bibtex_dict:
        sql_dict["isbn_issn"] = bibtex_dict["ISSN"]
    elif "ISBN" in bibtex_dict:
        sql_dict["isbn_issn"] = bibtex_dict["ISBN"]

    if "DOI" in bibtex_dict:
        sql_dict["doi"] = bibtex_dict["DOI"]

    if "url" in bibtex_dict:
        sql_dict["url"] = bibtex_dict["url"]

    sql_dict["bibtex_id"] = decide_bibtex_id(compose_bibtex_id(sql_dict["full_author"],sql_dict["year"]))

    return sql_dict


def main():
    list_of_references = import_bibtex_file('../bibtex_to_import.bib')

    max_id = decide_id(0)
    for reference in list_of_references.entries:

        if not do_exist(reference["year"],reference["author"],reference["title"]):
            sql_dict = bibtex_dict_to_sql_dict(reference, max_id)

            if new_entry(sql_dict):
                print "Importation was successful!!"
                print sql_dict["bibtex_id"]
            else:
                print "Not imported"

            max_id += 1




if __name__ == "__main__":
    sys.exit(main())
