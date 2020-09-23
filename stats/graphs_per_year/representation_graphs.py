import csv

colors_for_graphs = ["blue","red","green","orange","purple","brown"]

def print_csv_for_graph(dictionary_to_print, name_of_file):
    with open(name_of_file,'w') as f:
        writer = csv.writer(f, delimiter=',')
        for key,value in sorted(dictionary_to_print.iteritems()):
            writer.writerow([str(key),str(value)])

def replace_low_bars(str):
    result_str = str.replace('_',"\\_")
    return result_str

def represent_stacked_histogram(array_with_data, name_of_file_withoutextension):
    #The array has tuples of tuples with the following structure
    #[Type,[[year,value],[year,value]...], Type, [],...]
    with open(name_of_file_withoutextension+".tex",'w') as f:
        f.write("\\documentclass{article}\n\\usepackage{pgfplots}\n\\usepackage{filecontents}\n\\tikzset{>=latex}\n\\pgfrealjobname{papers_per_year}\n")
        f.write("\\begin{document}\n")
        f.write("\\beginpgfgraphicnamed{"+name_of_file_withoutextension+"}\n")
        f.write("\\begin{tikzpicture}\n")
        f.write("\\begin{axis}[ybar stacked,xlabel={Year},ylabel={Number of Papers},")
        f.write("grid=major,every axis plot/.append style={ultra thick},/pgf/number format/.cd,use comma,1000 sep={}]\n")

        for element in array_with_data:
            f.write("\\addplot coordinates\n")
            f.write("{")
            for element2 in element[1]:
                f.write("("+str(element2[0])+","+str(element2[1])+") ")
            f.write("};\n")

        #Now we print the labels in the legend
        f.write("\\legend{")
        counter = len(array_with_data)
        for element in array_with_data:
            f.write(element[0])
            if counter > 1:
                f.write(',')
                counter-=1

        f.write("}\n")
        f.write("\\end{axis}\n")
        f.write("\\end{tikzpicture}\n\\endpgfgraphicnamed\n\\end{document}")

def represent_separated_histogram(array_with_data, name_of_file_withoutextension):
    #The array has tuples of tuples with the following structure
    #[Type,[[year,value],[year,value]...], Type, [],...]
    with open(name_of_file_withoutextension+".tex",'w') as f:
        f.write("\\documentclass{article}\n")
        f.write("\\usepackage{pgfplots}\n")
        f.write("\\usepackage{filecontents}\n")
        f.write("\\usetikzlibrary{pgfplots.groupplots}")

        f.write("\\tikzset{>=latex}\n\\pgfrealjobname{papers_per_year}\n")
        f.write("\\begin{document}\n")
        f.write("\\beginpgfgraphicnamed{"+name_of_file_withoutextension+"}\n")
        f.write("\\begin{tikzpicture}\n")

        f.write("""\\begin{groupplot}[
                        group style={
                            group name=Number of papers per approach,
                            group size=1 by 5,
                            xlabels at=edge bottom,
                            xticklabels at=edge bottom,
                            vertical sep=0pt
                        },
                        ybar,
                        footnotesize,
                        width=8cm,
                        height=3cm,
                        xlabel=Year,
                        minor xtick = {2000,2001,...,2016,2017},
                        xtick = {2000,2004,...,2016},
                        xticklabels = {2000,2004,2008,2012,2016},
                        minor ytick = {0,1,...,6},
                        ytick = {2,4,6},
                        xmin=1999.5, xmax=2017.75,
                        ymin=0, ymax=7,
                        tickpos=left,
                        ytick align=outside,
                        xtick align=outside,
                        legend style={at={(1.05,0.5)},anchor=west, draw=none}
        ]\n""")

        color_counter = 0

        for element in array_with_data:
            f.write("\\nextgroupplot\n")
            f.write("\\addplot[fill="+colors_for_graphs[color_counter]+"] coordinates\n")
            f.write("{")
            for element2 in element[1]:
                f.write("("+str(element2[0])+","+str(element2[1])+") ")
            f.write("}; \\addlegendentry{"+element[0]+"};\n")

            if color_counter==0:
                f.write("\\coordinate (top) at (rel axis cs:0,1);\n")
            elif color_counter==4:
                f.write("\\coordinate (bot) at (rel axis cs:1,0);\n")

            color_counter+=1

        #Now we print the labels in the legend
        f.write("""\\end{groupplot}\n
            \\path (top)--(bot) coordinate[midway] (group center);\n
            \\node[above,rotate=90] at (group center -| current bounding box.west) {Number of papers};\n
            \\end{tikzpicture}\n
            \\endpgfgraphicnamed\n
            \\end{document}\n""")
