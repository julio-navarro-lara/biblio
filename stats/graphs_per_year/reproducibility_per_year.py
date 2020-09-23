import peewee as pw
import sys

sys.path.insert(0,'../../')

from models import Biblio

def count_reproducible_method_in_year(year):
    #Returns an array with the number of yes and no.
    return [
        Biblio.select().where(Biblio.reproducible_method.contains("yes")&(Biblio.year==year)&Biblio.main_objective.contains("detection")&Biblio.julio_state.contains("integrated_core")).count(),
        Biblio.select().where(Biblio.reproducible_method.contains("no")&(Biblio.year==year)&Biblio.main_objective.contains("detection")&Biblio.julio_state.contains("integrated_core")).count()
    ]

def count_reproducible_experiments_in_year(year):
    #Returns an array with the number of yes and no.
    return [
        Biblio.select().where(Biblio.reproducible_experiments.contains("yes")&(Biblio.year==year)&Biblio.main_objective.contains("detection")&Biblio.julio_state.contains("integrated_core")).count(),
        Biblio.select().where(Biblio.reproducible_experiments.contains("no")&(Biblio.year==year)&Biblio.main_objective.contains("detection")&Biblio.julio_state.contains("integrated_core")).count()
    ]

def count_accd_in_year(year):
    #Returns an array with the number of yes and no.
    return [
        Biblio.select().where(Biblio.av_dataset.contains("yes")&(Biblio.year==year)&Biblio.main_objective.contains("detection")&Biblio.julio_state.contains("integrated_core")).count(),
        Biblio.select().where(Biblio.av_dataset.contains("no")&(Biblio.year==year)&Biblio.main_objective.contains("detection")&Biblio.julio_state.contains("integrated_core")).count()
    ]

def count_acck_in_year(year):
    #Returns an array with the number of yes and no.
    return [
        Biblio.select().where(Biblio.av_knowledge.contains("yes")&(Biblio.year==year)&Biblio.main_objective.contains("detection")&Biblio.julio_state.contains("integrated_core")).count(),
        Biblio.select().where(Biblio.av_knowledge.contains("no")&(Biblio.year==year)&Biblio.main_objective.contains("detection")&Biblio.julio_state.contains("integrated_core")).count()
    ]

def count_mixed_reproducibility(year):
    return [
        Biblio.select().where(Biblio.reproducible_method.contains("yes")&Biblio.reproducible_experiments.contains("yes")&(Biblio.year==year)&Biblio.main_objective.contains("detection")&Biblio.julio_state.contains("integrated_core")).count(),
        Biblio.select().where(Biblio.reproducible_method.contains("yes")&Biblio.reproducible_experiments.contains("no")&(Biblio.year==year)&Biblio.main_objective.contains("detection")&Biblio.julio_state.contains("integrated_core")).count(),
        Biblio.select().where(Biblio.reproducible_method.contains("no")&Biblio.reproducible_experiments.contains("no")&(Biblio.year==year)&Biblio.main_objective.contains("detection")&Biblio.julio_state.contains("integrated_core")).count()
    ]

def count_for_all_years():
    total = 0
    for year in range(2001,2017):
        rep_method = count_reproducible_method_in_year(year)
        rep_experiments = count_reproducible_experiments_in_year(year)

        print "Year "+str(year)
        print "Reproducible Method: yes:"+str(rep_method[0])+" no:"+str(rep_method[1])
        print "Reproducible Experiments: yes:"+str(rep_experiments[0])+" no:"+str(rep_experiments[1])
        partial_total = rep_method[0]+rep_method[1]
        total += partial_total
        print "Total: "+str(partial_total)
        print ""

    print "***********"
    print "TOTAL: "+str(total)

def count_for_all_years_v2():
    total = 0
    output_stringA = "{"
    output_stringB = "{"
    output_stringC = "{"
    for year in range(2001,2017):
        results = count_mixed_reproducibility(year)

        partial_total = results[0]+results[1]+results[2]

        print "Year "+str(year)
        print "Reproducible Method & Experiment: "+str(results[0])+"\t"+str(round(float(results[0])*100/partial_total,1))
        print "Only Reproducible Method: "+str(results[1])+"\t"+str(round(float(results[1])*100/partial_total,1))
        print "Neither reproducible method nor experiment: "+str(results[2])+"\t"+str(round(float(results[2])*100/partial_total,1))

        total += partial_total
        print "Total: "+str(partial_total)
        print ""

        output_stringA += " ("+str(year)+','+str(results[0])+")"
        output_stringB += " ("+str(year)+','+str(results[1])+")"
        output_stringC += " ("+str(year)+','+str(results[2])+")"

    print "***********"
    print "TOTAL: "+str(total)
    print ""

    print output_stringA+" };"
    print output_stringB+" };"
    print output_stringC+" };"

def count_for_all_years_v3():
    total = 0
    output_stringA = "{"
    output_stringB = "{"
    output_stringC = "{"
    for year in range(2001,2017):
        results = count_mixed_reproducibility(year)

        partial_total = results[0]+results[1]+results[2]

        print "Year "+str(year)
        print "Reproducible Method & Experiment: "+str(results[0])+"\t"+str(round(float(results[0])*100/partial_total,1))

        total += partial_total
        print "Total: "+str(partial_total)
        print ""

        output_stringA += " ("+str(year)+','+str(round(float(results[0])*100/partial_total,1))+")"
        output_stringB += " ("+str(year)+','+str(partial_total)+")"

    print "***********"
    print "TOTAL: "+str(total)
    print ""

    print output_stringA+" };"
    print output_stringB+" };"
    print output_stringC+" };"

def count_for_all_years_v4():
    total = 0
    output_stringRep = "{"
    output_stringAccm = "{"
    output_stringAccd = "{"
    output_stringAcck = "{"
    for year in range(2001,2019):
        results_rep = count_reproducible_experiments_in_year(year)
        results_accm = count_reproducible_method_in_year(year)
        results_accd = count_accd_in_year(year)
        results_acck = count_acck_in_year(year)

        partial_total = Biblio.select().where((Biblio.year==year)&Biblio.main_objective.contains("detection")&Biblio.julio_state.contains("integrated_core")).count()

        print "Year "+str(year)
        print "Reproducible Experiment: "+str(results_rep[0])+"\t"+str(round(float(results_rep[0])*100/partial_total,1))

        total += partial_total
        print "Total: "+str(partial_total)
        print ""

        output_stringRep += " ("+str(year)+','+str(round(float(results_rep[0])*100/partial_total,1))+")"
        output_stringAccm += " ("+str(year)+','+str(round(float(results_accm[0])*100/partial_total,1))+")"
        output_stringAccd += " ("+str(year)+','+str(round(float(results_accd[0])*100/partial_total,1))+")"
        output_stringAcck += " ("+str(year)+','+str(round(float(results_acck[0])*100/partial_total,1))+")"

    print "***********"
    print "TOTAL: "+str(total)
    print ""

    print "Rep.:\t"+output_stringRep+" };"
    print "Accm:\t"+output_stringAccm+" };"
    print "Accd:\t"+output_stringAccd+" };"
    print "Acck:\t"+output_stringAcck+" };"

def main():
    count_for_all_years_v4()

if __name__ == "__main__":
    sys.exit(main())
