import csv

def represent_ranking_in_table_with_cite(array_of_tuples,number_of_items, name_of_file, description_phrase):

    with open(name_of_file,'w') as f:
        f.write("\\documentclass{article}\n")
        f.write("\\begin{document}\n")
        f.write("\\begin{table}[h!]\n")
        f.write("\\caption{"+description_phrase+"}\n")
        f.write("\\begin{tabular}{{||l|p{0.68\linewidth}|l|p{0.03\linewidth}||}\n")
        f.write("\\hline\n")
        f.write("Ref. & Title & Authors & Cit.\\\\ \\hline\n")
        for element in array_of_tuples:
            f.write("\\cite{"+element[0]+"} & "+element[1]+" & "+element[2]+" & "+str(element[3])+"\\\\\n")
        f.write("\\hline")
        f.write("\\end{tabular}\n")
        f.write("\\end{table}\n")
        f.write("\\end{document}")
    f.close()
    print array_of_tuples

def represent_ranking_in_table(array_of_tuples,number_of_items, name_of_file, description_phrase):

    with open(name_of_file,'w') as f:
        f.write("\\documentclass{article}\n")
        f.write("\\begin{document}\n")
        f.write("\\begin{table}[h!]\n")
        f.write("\\caption{Ranking of top "+str(number_of_items)+" entries according to "+description_phrase+"}\n")
        f.write("\\begin{tabular}{cccc}\n")
        f.write("\\hline\n")
        f.write("Reference & Number of citations\\\\ \\hline\n")
        for element in array_of_tuples:
            f.write(element[0].encode('utf-8')+" & "+str(element[1])+"\\\\\n")
        f.write("\\end{tabular}\n")
        f.write("\\end{table}\n")
        f.write("\\end{document}")
    f.close()
    print array_of_tuples

def replace_low_bars(str):
    result_str = str.replace('_',"\\_")
    return result_str
