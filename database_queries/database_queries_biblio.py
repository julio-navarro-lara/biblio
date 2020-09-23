#Copyright 2018 Julio Navarro
#Built at the University of Strasbourg (France). CSTB team @ ICube laboratory
import peewee as pw
import sys
import string
import unidecode


from models import Biblio

def decide_bibtex_id(first_try):
    lets_try = first_try
    list_of_letters = list(string.ascii_lowercase)
    counter = 1
    while Biblio.select().where(Biblio.bibtex_id==lets_try):
        lets_try = first_try[:2]+list_of_letters[counter]+first_try[2:]
        counter += 1
    return lets_try

def do_exist(year,full_author,title):
    if Biblio.select().where((Biblio.year == year)&(Biblio.title == title)&(Biblio.full_author == full_author)):
        print "The element already exists: " + str(year) + " " + full_author + " - " + title
        return True
    elif Biblio.select().where(Biblio.year == year and Biblio.title == title):
        print "ATTENTION: there is a reference with same year and title. WE ADD ANYWAYS"
        print str(year) + " " + full_author + " - " + title
        return False
    elif Biblio.select().where(Biblio.year == year and Biblio.full_author == full_author):
        print "ATTENTION: there is a reference with same year and authors. WE ADD ANYWAYS"
        print str(year) + " " + full_author + " - " + title
        return False
    else:
        return False

def new_entry(dict_entry):

    if "id" not in dict_entry:
        print "There is no id!!"
        print dict_entry
        return False
    if "full_author" not in dict_entry:
        print "There is no full_author!!"
        print dict_entry
        return False
    if "year" not in dict_entry:
        print "There is no year!!"
        print dict_entry
        return False
    if "bibtex_id" not in dict_entry:
        print "There is no bibtex_id!!"
        print dict_entry
        return False
    if "type" not in dict_entry:
        print "There is no type!!"
        print dict_entry
        return False
    if "title" not in dict_entry:
        print "There is no title!!"
        print dict_entry
        return False
    #if "author" not in dict_entry:
    #    print "There is no author!!"
    #    print dict_entry
    #    return False

    current_bibtex_id = unidecode.unidecode(dict_entry["bibtex_id"])

    Biblio.create(id=dict_entry["id"],
    full_author=dict_entry["full_author"].encode('utf-8'),
    year=dict_entry["year"],
    bibtex_id=current_bibtex_id,
    type = dict_entry["type"],
    title = dict_entry["title"].encode('utf-8'))
    #author = dict_entry["author"].encode('utf-8'))

    if "journal" in dict_entry:
        update_journal(current_bibtex_id, dict_entry["journal"])
    if "publisher" in dict_entry:
        update_publisher(current_bibtex_id, dict_entry["publisher"])
    if "volume" in dict_entry:
        update_volume(current_bibtex_id, dict_entry["volume"])
    if "issue" in dict_entry:
        update_issue(current_bibtex_id, dict_entry["issue"])
    if "pages" in dict_entry:
        update_pages(current_bibtex_id, dict_entry["pages"])
    if "isbn_issn" in dict_entry:
        update_isbn_issn(current_bibtex_id, dict_entry["isbn_issn"])
    if "doi" in dict_entry:
        update_doi(current_bibtex_id, dict_entry["doi"])

    return True

def update_journal(bibtex_id, new_journal):
    query = Biblio.update(journal=new_journal.encode('utf-8')).where(Biblio.bibtex_id == bibtex_id)
    query.execute()

def update_publisher(bibtex_id, new_publisher):
    query = Biblio.update(publisher=new_publisher.encode('utf-8')).where(Biblio.bibtex_id == bibtex_id)
    query.execute()

def update_volume(bibtex_id, new_volume):
    query = Biblio.update(volume=new_volume).where(Biblio.bibtex_id == bibtex_id)
    query.execute()

def update_issue(bibtex_id, new_issue):
    query = Biblio.update(issue=new_issue).where(Biblio.bibtex_id == bibtex_id)
    query.execute()

def update_pages(bibtex_id, new_pages):
    query = Biblio.update(pages=new_pages).where(Biblio.bibtex_id == bibtex_id)
    query.execute()

def update_isbn_issn(bibtex_id, new_isbn_issn):
    query = Biblio.update(isbn_issn=new_isbn_issn).where(Biblio.bibtex_id == bibtex_id)
    query.execute()

def update_doi(bibtex_id, new_doi):
    query = Biblio.update(doi=new_doi).where(Biblio.bibtex_id == bibtex_id)
    query.execute()

def update_citations_google(bibtex_id, num_citations):
    query = Biblio.update(citations_google=num_citations).where(Biblio.bibtex_id == bibtex_id)
    query.execute()

def update_url(bibtex_id, new_url):
    query = Biblio.update(url=new_url).where(Biblio.bibtex_id == bibtex_id)
    query.execute()

def update_url_pdf(bibtex_id, new_url_pdf):
    query = Biblio.update(url_pdf=new_url_pdf).where(Biblio.bibtex_id == bibtex_id)
    query.execute()

def update_clusterid_google(bibtex_id, new_clusterid_google):
    query = Biblio.update(clusterid_google=new_clusterid_google).where(Biblio.bibtex_id == bibtex_id)
    query.execute()

def update_bibtex_reference(bibtex_id, new_bibtex_reference):
    query = Biblio.update(bibtex_reference=new_bibtex_reference).where(Biblio.bibtex_id == bibtex_id)
    query.execute()

def update_raw_bibliography(bibtex_id, new_raw_bibliography):
    query = Biblio.update(raw_bibliography=new_raw_bibliography).where(Biblio.bibtex_id == bibtex_id)
    query.execute()

def update_plain_text_reference(bibtex_id, new_plain_text_reference):
    query = Biblio.update(plain_text_reference=new_plain_text_reference).where(Biblio.bibtex_id == bibtex_id)
    query.execute()

def main():
    print "test"
    #update_citations_google('99_Huang',10000)
    #update_url('99_Huang', 'cualquier cosa')
    #update_url_pdf('99_Huang', 'cualquier cosa')
    #update_clusterid_google('99_Huang', 'cualquier cosa')

if __name__ == "__main__":
    sys.exit(main())
