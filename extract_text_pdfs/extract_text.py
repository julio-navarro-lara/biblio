#Copyright 2018 Julio Navarro
#Built at the University of Strasbourg (France). CSTB team @ ICube laboratory
import textract
from os import path
from glob import glob

def find_ext(dr, ext):
    return glob(path.join(dr,"*.{}".format(ext)))

def main():
    list_files = find_ext("/Users/Julio/Documents/PhD/Papers/Security/Multi-Step attacks DB/Corpus/","pdf")

    for filepath in list_files:
        output_name = filepath.rsplit('/',1)[1].split('.',1)[0]
        print "Processing "+output_name+"..."
        try:
            text = textract.process(filepath,encoding='utf-8')
            with open("output/"+output_name+".txt",'w') as f:
                f.write(text)
        except UnicodeDecodeError:
            print "CANNOT DECODE "+output_name

if __name__=="__main__":
    main()
