import peewee as pw
import sys
import operator
from representation_ranking import represent_ranking_in_table_with_cite

sys.path.insert(0,'../../')

from models import Biblio

selection = Biblio.select().where((Biblio.main_objective=='detection')&(Biblio.julio_state.contains("integrated")))

def extract_citations():
    bibtex_citations = {}
    for reference in selection:
        if reference.citations_google:
            bibtex_citations[reference.bibtex_id] = int(reference.citations_google)
            print reference.bibtex_id.decode("utf-8") + "\t" + str(reference.citations_google)

    return sort_dictionary(bibtex_citations)

def sort_dictionary(entry_dictionary):
    #it sorts a dictionary by value in the reverse mode and returns an array of tuples, with the first element the key and the second the value
    return sorted(entry_dictionary.items(), key=operator.itemgetter(1), reverse=True)

def select_top(array_to_select,number_of_items):
    return array_to_select[0:number_of_items]

#     %\begin{table}[h!]
# %\caption{Sample table title. This is where the description of the table should go.}
# %      \begin{tabular}{cccc}
# %        \hline
# %           & B1  &B2   & B3\\ \hline
# %        A1 & 0.1 & 0.2 & 0.3\\
# %        A2 & ... & ..  & .\\
# %        A3 & ..  & .   & .\\ \hline
# %      \end{tabular}
# %\end{table}

def make_array_richer(array):
    result = []
    for element in array:
        entry = Biblio.get(Biblio.bibtex_id==element[0])
        result.append([element[0],entry.title,entry.author,element[1]])

    return result

def main():
    number_of_items = 20
    array_to_represent = select_top(extract_citations(),number_of_items)
    richer_array = make_array_richer(array_to_represent)
    represent_ranking_in_table_with_cite(richer_array,number_of_items,'ranking_citations.tex','Ranking of top '+str(number_of_items)+' entries according to the number of citations in Google Scholar')

if __name__ == "__main__":
    sys.exit(main())
