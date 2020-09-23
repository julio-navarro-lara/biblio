#Copyright 2018 Julio Navarro
#Built at the University of Strasbourg (France). CSTB team @ ICube laboratory
import peewee as pw
import sys
import string
import unidecode

sys.path.insert(0,'../')

from models import AuthorDetect

def get_max_id():
    selection = AuthorDetect.select(AuthorDetect.id)
    max_id = 1
    for element in selection:
        if element.id > max_id:
            max_id = element.id
    return max_id

def do_exist(author):
    register = AuthorDetect.select().where(AuthorDetect.author == author)
    if register:
        print "The element already exists: " + author
        return register.id
    else:
        return 0

def check_dict_entry(dict_entry):
    if "id" not in dict_entry:
        print "There is no id!!"
        print dict_entry
        return False
    if "author" not in dict_entry:
        print "There is no author!!"
        print dict_entry
        return False
    if "references" not in dict_entry:
        print "There is no references!!"
        print dict_entry
        return False
    if "num_papers" not in dict_entry:
        print "There is no num_papers!!"
        print dict_entry
        return False
    if "total_citations" not in dict_entry:
        print "There is no total_citations!!"
        print dict_entry
        return False
    if "max_citations" not in dict_entry:
        print "There is no max_citations!!"
        print dict_entry
        return False
    if "min_citations" not in dict_entry:
        print "There is no min_citations!!"
        print dict_entry
        return False
    if "coauthors" not in dict_entry:
        print "There is no coauthors!!"
        print dict_entry
        return False

    return True

def new_entry(dict_entry):
    if not check_dict_entry(dict_entry):
        return False

    AuthorDetect.create(id=dict_entry["id"],
    author=dict_entry["author"].encode('utf-8'),
    references=dict_entry["references"],
    num_papers=dict_entry["num_papers"],
    total_citations=dict_entry["total_citations"],
    max_citations=dict_entry["max_citations"],
    min_citations=dict_entry["min_citations"],
    coauthors = dict_entry["coauthors"].encode('utf-8'))

    return True

def new_entry_safe(dict_entry):
    existent_id = do_exist(dict_entry["author"])
    if existent_id == 0:
        did_it_work = new_entry(dict_entry)
        if not did_it_work:
            print "We could not create the entry"
            return False
        return True
    else:
        update_entry(existent_id, dict_entry)
        return False

def update_entry(id, dict_entry):
    entry = AuthorDetect.select().where(AuthorDetect.id == id).get()
    entry.references = dict_entry["references"]
    entry.num_papers=dict_entry["num_papers"]
    entry.total_citations=dict_entry["total_citations"]
    entry.max_citations=dict_entry["max_citations"]
    entry.min_citations=dict_entry["min_citations"]
    entry.coauthors = dict_entry["coauthors"].encode('utf-8')
    entry.save()

def main():
    print "test"
    #update_citations_google('99_Huang',10000)
    #update_url('99_Huang', 'cualquier cosa')
    #update_url_pdf('99_Huang', 'cualquier cosa')
    #update_clusterid_google('99_Huang', 'cualquier cosa')

if __name__ == "__main__":
    sys.exit(main())
