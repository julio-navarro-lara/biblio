import csv

def replace_low_bars(str):
    result_str = str.replace('_',"\\_")
    return result_str

def represent_pie(array_with_data, name_of_file_withoutextension):
    #The array has tuples whose first value is the name of the fields in the pie chart, and the second value the %
    with open(name_of_file_withoutextension+".tex",'w') as f:
        f.write("\\documentclass{article}\n\\usepackage{pgfplots}\n\\usepackage{filecontents}\n\\usepackage{pgf-pie}\n\\tikzset{>=latex}\n\\pgfrealjobname{plottemporal}\n")
        f.write("\\begin{document}\n")
        f.write("\\beginpgfgraphicnamed{"+name_of_file_withoutextension+"}\n")
        f.write("\\begin{tikzpicture}")
        f.write("\\pie{")
        counter = len(array_with_data)
        for element in array_with_data:
            f.write(str(element[1])+"/"+replace_low_bars(element[0]))
            if counter > 1:
                f.write(',')
                counter -= 1

        f.write("}\n")
        f.write("\\end{tikzpicture}\n\\endpgfgraphicnamed\n\\end{document}")
