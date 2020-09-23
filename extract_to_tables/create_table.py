#Copyright 2018 Julio Navarro
#Built at the University of Strasbourg (France). CSTB team @ ICube laboratory
import peewee as pw
import sys

sys.path.insert(0,'../')

from models import AuthorDetect

def main():
    try:
        AuthorDetect.create_table()
    except pw.OperationalError:
        print "Table already exists!"

if __name__ == "__main__":
    sys.exit(main())
