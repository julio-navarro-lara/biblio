#Copyright 2018 Julio Navarro
#Built at the University of Strasbourg (France). CSTB team @ ICube laboratory
from scholar import *
import peewee as pw

sys.path.insert(0,'../')
sys.path.insert(0,'../database_queries/')

from models import Biblio
from database_queries_biblio import *

from random import randint
from time import sleep


querier = ScholarQuerier()
settings = ScholarSettings()

def get_csv(querier, header=False, sep='|'):
    articles = querier.articles
    for art in articles:
        result = art.as_csv(header=header, sep=sep)
        header = False
        return encode(result)

def do_query(title, query):

    query.set_phrase(title)

    querier.send_query(query)

    return get_csv(querier)
    #txt(querier, with_globals=None)

def split_citation(text):
    return text.split('|')

def extract_citation_number_for_the_non_found():

    #We only select those records with NUll in the URL
    selection = Biblio.select(Biblio.title, Biblio.bibtex_id).where(Biblio.citations_google.is_null())

    querier.apply_settings(settings)

    query = SearchScholarQuery()

    element = selection[0]

    for element in selection:

        full_csv = do_query("\""+element.title+"\"", query)
        print "*******************"
        print "TITLE: "+element.title
        print full_csv
        print "*******************"

        array_of_citation = split_citation(full_csv)

        update_url(element.bibtex_id,array_of_citation[1])
        update_citations_google(element.bibtex_id,array_of_citation[3])
        update_clusterid_google(element.bibtex_id,array_of_citation[5])
        update_url_pdf(element.bibtex_id,array_of_citation[6])

        waiting_time = randint(10,100)

        for i in range(waiting_time,0,-1):
            sys.stdout.write(str(i)+", ")
            sys.stdout.flush()
            sleep(1)

    #URL is in position 1
    #PDF URL is in position 6
    #Number of citations is in position 3
    #Cluster ID is in position 5

    #We have to modify the SQL database
    #Wait for doing the tests until Google Scholar free our IP

def extract_citation_number_for_all():

    #We update all the registers, even if they already have a number of citations
    selection = Biblio.select(Biblio.title, Biblio.bibtex_id)

    querier.apply_settings(settings)

    query = SearchScholarQuery()

    element = selection[0]

    centinela = 1

    for element in selection:

        full_csv = do_query("\""+element.title+"\"", query)
        print "*******************"
        print "TITLE: "+element.title
        print full_csv
        print "*******************"

        array_of_citation = split_citation(full_csv)

        update_url(element.bibtex_id,array_of_citation[1])
        update_citations_google(element.bibtex_id,array_of_citation[3])
        update_clusterid_google(element.bibtex_id,array_of_citation[5])
        update_url_pdf(element.bibtex_id,array_of_citation[6])

        print "Iteration "+str(centinela)
        centinela += 1

        waiting_time = randint(10,100)

        for i in range(waiting_time,0,-1):
            sys.stdout.write(str(i)+", ")
            sys.stdout.flush()
            sleep(1)

    #URL is in position 1
    #PDF URL is in position 6
    #Number of citations is in position 3
    #Cluster ID is in position 5

def main():
    extract_citation_number_for_all()
    #extract_citation_number_for_the_non_found()


    #citation text:
    #A stochastic game theoretic approach to attack prediction and optimal active defense strategy decision|http://ieeexplore.ieee.org/abstract/document/4525297/|2008|17|3|17302765911397515927|None|http://scholar.google.com/scholar?cites=17302765911397515927&as_sdt=2005&sciodt=0,5&hl=en|http://scholar.google.com/scholar?cluster=17302765911397515927&hl=en&as_sdt=0,5|None|Abstract: This paper presents a stochastic game theoretic approach to analyzing attack prediction and the active defense of computer networks. A Markov chain for privilege (MCP) model to predict attacker&#39;s behavior and strategies is proposed. We regard the interactions between an attacker and the defender as a two-player, non-cooperative, zero-sum, finite stochastic game and formulate an attack-defense stochastic game (ADSG) model for the  ...

if __name__ == "__main__":
    sys.exit(main())
