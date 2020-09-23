import peewee as pw
import sys

sys.path.insert(0,'../../')

from models import Biblio
from representation_graphs import *

def extract_number_of_papers_per_year(begin_year, end_year):

    result = {}

    total = 0

    for i in range(begin_year,end_year):
        number_of_papers = Biblio.select().where((Biblio.year==i)&(Biblio.main_objective == 'detection')&(Biblio.julio_state.contains("integrated_core"))).count()
        result[i] = number_of_papers
        print str(i)+"  "+str(number_of_papers)
        total += number_of_papers

    print " "
    print "TOTAL: "+str(total)
    return result

def main():
    result = extract_number_of_papers_per_year(1999,2019)
    print_csv_for_graph(result,"papers_per_year.csv")

if __name__ == "__main__":
    sys.exit(main())
