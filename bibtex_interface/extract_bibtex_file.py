#!/usr/bin/env python
#Copyright 2018 Julio Navarro
#Built at the University of Strasbourg (France). CSTB team @ ICube laboratory
# -*- coding: utf-8 -*-

import peewee as pw
import sys

sys.path.insert(0,'../')
sys.path.insert(0,'../database_queries/')

from database_queries_biblio import *
from models import Biblio

selection = Biblio.select()#.where(Biblio.julio_state != "Excluded")

def clean_string(dirty_string):
    result = dirty_string.replace("&", "\\&")
    return result

def building_bibtex_conference(element):
    result = "@inproceedings{"+element.bibtex_id+",\n"
    if not element.bibtex_full_author:
        print "Empty authors in "+element.bibtex_id
    else:
        result += "\tauthor={"+clean_string(element.bibtex_full_author)+"},\n"
    if not element.bibtex_title:
        print "Empty title in "+element.bibtex_id
    else:
        result += "\ttitle={"+clean_string(element.bibtex_title)+"},\n"
    if not element.journal:
        print "Empty conference in "+element.bibtex_id
    else:
        result += "\tbooktitle={"+clean_string(element.journal)+"},\n"

    if element.place:
        result += "\taddress={"+clean_string(element.place)+"},\n"
    if element.bibtex_publisher:
        result += "\tpublisher={"+clean_string(element.bibtex_publisher)+"},\n"
    if element.volume:
        result += "\tvolume={"+clean_string(element.volume)+"},\n"
    if element.pages:
        result += "\tpages={"+clean_string(element.pages)+"},\n"
    if element.isbn_issn:
        result += "\tISBN={"+clean_string(element.isbn_issn)+"},\n"
    if element.doi:
        result += "\tDOI={"+clean_string(element.doi)+"},\n"
    #if element.url or element.url!=None:
    #    result += "\turl={"+clean_string(element.url)+"},\n"

    result += "\tyear={"+str(element.year)+"},\n"

    if not element.year:
        print "Empty year in "+element.bibtex_id

    result += "\ttype={"+clean_string(element.type)+"},\n"
    result += "}\n"
    return result.encode('utf-8')

def building_bibtex_journal(element):
    result = "@article{"+element.bibtex_id+",\n"

    if not element.bibtex_full_author:
        print "Empty authors in "+element.bibtex_id
    else:
        result += "\tauthor={"+clean_string(element.bibtex_full_author)+"},\n"

    if not element.bibtex_title:
        print "Empty title in "+element.bibtex_id
    else:
        result += "\ttitle={"+clean_string(element.bibtex_title)+"},\n"

    if not element.journal:
        print "Empty journal in "+element.bibtex_id
    else:
        result += "\tjournal={"+clean_string(element.journal)+"},\n"

    if element.volume:
        result += "\tvolume={"+clean_string(element.volume)+"},\n"
    if element.issue:
        result += "\tnumber={"+clean_string(element.issue)+"},\n"
    if element.pages:
        result += "\tpages={"+clean_string(element.pages)+"},\n"
    if element.isbn_issn:
        result += "\tISSN={"+clean_string(element.isbn_issn)+"},\n"
    if element.doi:
        result += "\tDOI={"+clean_string(element.doi)+"},\n"
    # if element.url or element.url!=None:
    #     result += "\turl={"+clean_string(element.url)+"},\n"

    result += "\tyear={"+str(element.year)+"},\n"

    if not element.year:
        print "Empty year in "+element.bibtex_id

    result += "\ttype={"+clean_string(element.type)+"},\n"
    result += "}\n"
    return result.encode('utf-8')

def building_bibtex_booksection(element):
    result = "@inbook{"+element.bibtex_id+",\n"
    result += "\tauthor={"+clean_string(element.bibtex_full_author)+"},\n"
    if not element.bibtex_full_author:
        print "Empty authors in "+element.bibtex_id
    result += "\ttitle={"+clean_string(element.bibtex_title)+"},\n"
    if not element.bibtex_title:
        print "Empty title in "+element.bibtex_id
    result += "\tbooktitle={"+clean_string(element.journal)+"},\n"
    if not element.journal:
        print "Empty booktitle in "+element.bibtex_id

    result += "\tpublisher={"+clean_string(element.bibtex_publisher)+"},\n"
    if not element.bibtex_publisher:
        print "Empty publisher in "+element.bibtex_id

    result += "\tpages={"+clean_string(element.pages)+"},\n"
    if not element.pages:
        print "Empty pages in "+element.bibtex_id

    if element.volume:
        result += "\tvolume={"+clean_string(element.volume)+"},\n"
    if element.isbn_issn:
        result += "\tISSN={"+clean_string(element.isbn_issn)+"},\n"
    if element.doi:
        result += "\tDOI={"+clean_string(element.doi)+"},\n"
    # if element.url or element.url!=None:
    #     result += "\turl={"+clean_string(element.url)+"},\n"

    result += "\tyear={"+str(element.year)+"},\n"

    if not element.year:
        print "Empty year in "+element.bibtex_id

    result += "\ttype={"+clean_string(element.type)+"},\n"
    result += "}\n"
    return result.encode('utf-8')

def building_bibtex_thesis(element):
    result = "@phdthesis{"+element.bibtex_id+",\n"

    if not element.bibtex_full_author:
        print "Empty authors in "+element.bibtex_id
    else:
        result += "\tauthor={"+clean_string(element.bibtex_full_author)+"},\n"

    if not element.bibtex_title:
        print "Empty title in "+element.bibtex_id
    else:
        result += "\ttitle={"+clean_string(element.bibtex_title)+"},\n"

    if not element.bibtex_publisher:
        print "Empty school in "+element.bibtex_id
    else:
        result += "\tschool={"+clean_string(element.bibtex_publisher)+"},\n"

    if element.doi:
        result += "\tDOI={"+clean_string(element.doi)+"},\n"
    # if element.url or element.url!=None:
    #     result += "\turl={"+clean_string(element.url)+"},\n"

    result += "\tyear={"+str(element.year)+"},\n"

    if not element.year:
        print "Empty year in "+element.bibtex_id

    result += "\ttype={"+clean_string(element.type)+"},\n"
    result += "}\n"
    return result.encode('utf-8')

def building_bibtex_report(element):
    result = "@techreport{"+element.bibtex_id+",\n"
    if not element.bibtex_full_author:
        print "Empty authors in "+element.bibtex_id
    else:
        result += "\tauthor={"+clean_string(element.bibtex_full_author)+"},\n"
    if not element.bibtex_title:
        print "Empty title in "+element.bibtex_id
    else:
        result += "\ttitle={"+clean_string(element.bibtex_title)+"},\n"
    if not element.bibtex_publisher:
        print "Empty institution in "+element.bibtex_id
    else:
        result += "\tinstitution={"+clean_string(element.bibtex_publisher)+"},\n"


    if element.doi:
        result += "\tDOI={"+clean_string(element.doi)+"},\n"
    # if element.url or element.url!=None:
    #     result += "\turl={"+clean_string(element.url)+"},\n"

    result += "\tyear={"+str(element.year)+"},\n"

    if not element.year:
        print "Empty year in "+element.bibtex_id

    result += "\ttype={"+clean_string(element.type)+"},\n"
    result += "}\n"
    return result.encode('utf-8')

def building_bibtex_book(element):
    result = "@book{"+element.bibtex_id+",\n"

    if not element.bibtex_full_author:
        print "Empty authors in "+element.bibtex_id
    else:
        result += "\tauthor={"+clean_string(element.bibtex_full_author)+"},\n"

    if not element.bibtex_title:
        print "Empty title in "+element.bibtex_id
    else:
        result += "\ttitle={"+clean_string(element.bibtex_title)+"},\n"

    if not element.bibtex_publisher:
        print "Empty publisher in "+element.bibtex_id
    else:
        result += "\tpublisher={"+clean_string(element.bibtex_publisher)+"},\n"

    if element.volume:
        result += "\tvolume={"+clean_string(element.volume)+"},\n"
    if element.doi:
        result += "\tDOI={"+clean_string(element.doi)+"},\n"
    # if element.url or element.url!=None:
    #     result += "\turl={"+clean_string(element.url)+"},\n"

    result += "\tyear={"+str(element.year)+"},\n"

    if not element.year:
        print "Empty year in "+element.bibtex_id

    result += "\ttype={"+clean_string(element.type)+"},\n"
    result += "}\n"
    return result.encode('utf-8')

def building_bibtex_web(element):
    result = "@misc{"+element.bibtex_id+",\n"

    if element.bibtex_full_author:
        result += "\tauthor={"+clean_string(element.bibtex_full_author)+"},\n"
    if element.bibtex_title:
        result += "\ttitle={"+clean_string(element.bibtex_title)+"},\n"
    if element.bibtex_publisher:
        result += "\tpublisher={"+clean_string(element.bibtex_publisher)+"},\n"
    if element.doi:
        result += "\tDOI={"+clean_string(element.doi)+"},\n"
    # if element.url or element.url!=None:
    #     result += "\turl={"+clean_string(element.url)+"},\n"

    if not element.url:
        print "Empty URL in "+element.bibtex_id
    else:
        result += "\turl={"+str(element.url)+"},\n"

    if not element.year:
        print "Empty year in "+element.bibtex_id
    else:
        result += "\tyear={"+str(element.year)+"},\n"

    if not element.date:
        print "Empty date accessed in "+element.bibtex_id
    else:
        result += "note\t={(Date last accessed "+str(element.date)+")},\n"

    result += "\ttype={"+clean_string(element.type)+"},\n"
    result += "}\n"
    return result.encode('utf-8')

def building_bibtex_misc(element):
    result = "@misc{"+element.bibtex_id+",\n"

    if element.bibtex_full_author:
        result += "\tauthor={"+clean_string(element.bibtex_full_author)+"},\n"
    if element.bibtex_title:
        result += "\ttitle={"+clean_string(element.bibtex_title)+"},\n"
    if element.bibtex_publisher:
        result += "\tpublisher={"+clean_string(element.bibtex_publisher)+"},\n"
    if element.volume:
        result += "\tvolume={"+clean_string(element.volume)+"},\n"
    if element.doi:
        result += "\tDOI={"+clean_string(element.doi)+"},\n"
    # if element.url or element.url!=None:
    #     result += "\turl={"+clean_string(element.url)+"},\n"

    result += "\tyear={"+str(element.year)+"},\n"

    if not element.year:
        print "Empty year in "+element.bibtex_id

    result += "\ttype={"+clean_string(element.type)+"},\n"
    result += "}\n"
    return result.encode('utf-8')

def extracting_bibtex_file(filename):
    there_are_journal = False
    there_are_conferenceproceedings = False
    there_are_book_section = False
    there_are_thesis = False
    there_are_reports = False
    there_are_books = False
    there_are_webs = False
    there_are_other_things = False

    with open(filename, 'w') as f:
        for element in selection:
            if element.type == "Conference Proceedings":
                reference_text = building_bibtex_conference(element)
                there_are_conferenceproceedings = True
            elif element.type == "Journal Article":
                reference_text = building_bibtex_journal(element)
                there_are_journal = True
            elif element.type == "Book Section":
                reference_text = building_bibtex_booksection(element)
                there_are_book_section = True
            elif element.type == "Thesis":
                reference_text = building_bibtex_thesis(element)
                there_are_thesis = True
            elif element.type == "Report":
                reference_text = building_bibtex_report(element)
                there_are_reports = True
            elif element.type == "Book":
                reference_text = building_bibtex_book(element)
                there_are_books = True
            elif element.type == "Web":
                reference_text = building_bibtex_web(element)
                there_are_webs = True
            else:
                print "There is a misc type: "+element.type
                reference_text = building_bibtex_misc(element)
                there_are_other_things = True

            f.write(reference_text)
            update_reference_in_db(element.bibtex_id,reference_text)


    if there_are_conferenceproceedings:
        print "There are Conference Proceedings"
    if there_are_journal:
        print "There are Journals"
    if there_are_book_section:
        print "There are Book Sections"
    if there_are_thesis:
        print "There are Thesis"
    if there_are_reports:
        print "There are Reports"
    if there_are_books:
        print "There are Books"
    if there_are_webs:
        print "There are Webs"
    if there_are_other_things:
        print "There are other things!!"

def update_reference_in_db(bibtex_id, text):
    update_bibtex_reference(bibtex_id, text)

def main():
    extracting_bibtex_file("/Users/Julio/Documents/PhD/Mis papers/Bibliography Computers and Security/bibliography_multistep.bib")

if __name__ == "__main__":
    sys.exit(main())
