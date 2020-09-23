#Copyright 2018 Julio Navarro
#Built at the University of Strasbourg (France). CSTB team @ ICube laboratory
import peewee as pw
import sys

sys.path.insert(0,'../')
sys.path.insert(0,'../database_queries/')

from models import Biblio
from database_queries_authordetect import get_max_id,new_entry_safe

selection = Biblio.select().where((Biblio.main_objective == 'detection')&(Biblio.julio_state.contains("integrated")))

def extract_authors():
    author_dict = {}
    for reference in selection:
        array_of_authors = [x.strip() for x in reference.full_author.split(' and ')]

        citations = reference.citations_google
        bibtex_id = reference.bibtex_id

        for author in array_of_authors:
            #We need an array only with the rest of the authors
            other_authors = list(array_of_authors)
            other_authors.remove(author)
            if author not in author_dict:
                author_dict[author] = [[bibtex_id],
                                        1,
                                        citations,
                                        citations,
                                        citations,
                                        other_authors]
            else:
                copied_data = list(author_dict[author])
                #We add the id to the list of papers of this author
                copied_data[0].append(bibtex_id)
                #We add another paper to the list
                copied_data[1] += 1
                #we add the number of citations
                copied_data[2] += citations
                #Max number of citations in one paper
                if citations > copied_data[3]:
                    copied_data[3] = citations
                #Min number of citations in one paper
                if citations < copied_data[4]:
                    copied_data[4] = citations
                for element in other_authors:
                    if element not in copied_data[5]:
                        copied_data[5].append(element)

                author_dict[author] = copied_data

    return author_dict

def print_results(author_dict):
    for author in author_dict:
        print author
        print author_dict[author]

def author_entry_to_dict(author,id,content):
    result={}

    result["id"] = id
    result["author"] = author
    result["references"] = array_to_semicolon_separated(content[0])
    result["num_papers"] = content[1]
    result["total_citations"] = content[2]
    result["max_citations"] = content[3]
    result["min_citations"] = content[4]
    if content[5]:
        result["coauthors"] = array_to_semicolon_separated(content[5])
    else:
        print content[5]
        result["coauthors"] = "ANOTHING"

    return result

def array_to_semicolon_separated(input):
    result = input[0]

    for element in input[1:]:
        result += ";"
        result += element

    return result

def populate_table(dict_of_authors):
    chosen_id = get_max_id()
    for author in dict_of_authors:
        author_dict = author_entry_to_dict(author,chosen_id,dict_of_authors[author])
        was_a_new_one = new_entry_safe(author_dict)
        if was_a_new_one:
            chosen_id += 1


def main():

     dict_of_authors = extract_authors()
     populate_table(dict_of_authors)

if __name__ == "__main__":
    sys.exit(main())
