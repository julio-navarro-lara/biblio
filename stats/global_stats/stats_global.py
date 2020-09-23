import peewee as pw
import sys

sys.path.insert(0,'../../')

from models import Biblio

def get_count_of_main_objective(value):
    return Biblio.select().where((Biblio.main_objective.contains(value))&(Biblio.julio_state.contains("integrated"))).count()

def get_count_of_julio_state(value):
    return Biblio.select().where(Biblio.julio_state.contains(value)).count()

def get_count_of_julio_state_and_main_objective(value_state, value_objective):
    return Biblio.select().where((Biblio.julio_state.contains(value_state))
    &(Biblio.main_objective.contains(value_objective))).count()

def output_stats():
    query = "detection"
    print "Number of integrated papers with:"

    print "  main_objective="+query+": "+str(get_count_of_main_objective(query))

    print "  belongs to the core of multi-step attack : "+str(get_count_of_julio_state("_core_"))

    print "  are integrated in the paper: "+str(get_count_of_julio_state("integrated"))

    print " "

    print "Number of integrated papers in each phase: "
    print "  Phase B: "+str(get_count_of_julio_state("_B"))
    print "  Phase C1: "+str(get_count_of_julio_state("_C1"))
    print "  Phase C2: "+str(get_count_of_julio_state("_C2"))
    print "  Phase CitedBy: "+str(get_count_of_julio_state("_citedby"))

    print "Number of integrated papers about DETECTION in each phase: "
    print "  Phase B: "+str(get_count_of_julio_state_and_main_objective("integrated_core_B","detection"))
    print "  Phase C1: "+str(get_count_of_julio_state_and_main_objective("integrated_core_C1","detection"))
    print "  Phase C2: "+str(get_count_of_julio_state_and_main_objective("integrated_core_C2","detection"))
    print "  Phase CitedBy: "+str(get_count_of_julio_state_and_main_objective("integrated_core_citedby","detection"))


def main():
    output_stats()

if __name__ == "__main__":
    sys.exit(main())
