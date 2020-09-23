#Copyright 2018 Julio Navarro
#Built at the University of Strasbourg (France). CSTB team @ ICube laboratory
import peewee as pw
import csv

db = pw.SqliteDatabase("/Users/Julio/programming/python/managing_bibliography/version_2_0_writing_thesis/biblio.db")

class BaseModel(pw.Model):
    class Meta:
        database = db

class Biblio(BaseModel):
    id = pw.IntegerField(null=True)
    type = pw.TextField()
    author = pw.TextField()
    year = pw.IntegerField(null=True)
    title = pw.TextField()
    journal = pw.TextField(null=True)
    place = pw.TextField(null=True)
    publisher = pw.TextField(null=True)
    volume = pw.TextField(null=True)
    issue = pw.TextField(null=True)
    pages = pw.TextField(null=True)
    date = pw.TextField(null=True)
    isbn_issn = pw.TextField(null=True)
    doi = pw.TextField(null=True)
    bibtex_id = pw.TextField(null=True)
    citations_google = pw.IntegerField(null=True)
    origin = pw.TextField(null=True)
    keywords = pw.TextField(null=True)
    abstract = pw.TextField(null=True)
    evaluation = pw.TextField(null=True)
    theme_endnote = pw.TextField(null=True)
    tags = pw.TextField(null=True)
    dataset = pw.TextField(null=True)
    bibliography = pw.TextField(null=True)
    type_data = pw.TextField(null=True)
    type_experiment = pw.TextField(null=True)
    julio_state = pw.TextField(null=True)
    main_objective = pw.TextField(null=True)
    approach = pw.TextField(null=True)
    knowledge_extraction = pw.TextField(null=True)
    clusterid_google = pw.TextField(null=True)
    url = pw.TextField(null=True)
    url_pdf = pw.TextField(null=True)
    reproducible_method = pw.TextField(null=True)
    attack_model = pw.TextField(null=True)
    reproducible_experiments = pw.TextField(null=True)
    full_author = pw.TextField(null=True)
    context_information_for_linking = pw.TextField(null=True)
    bibtex_title = pw.TextField(null=True)
    bibtex_full_author = pw.TextField(null=True)
    bibtex_publisher = pw.TextField(null=True)
    bibtex_reference = pw.TextField(null=True)
    raw_bibliography = pw.TextField(null=True)
    plain_text_reference = pw.TextField(null=True)
    general_approach = pw.TextField(null=True)
    group = pw.TextField(null=True)
    av_dataset = pw.TextField(null=True)
    av_knowledge = pw.TextField(null=True)
    name_method = pw.TextField(null=True)
    cited_by_checked = pw.TextField(null=True)
    attack_activity_location = pw.TextField(null=True)
    attack_agent = pw.TextField(null=True)
    attack_evidence = pw.TextField(null=True)
    attack_focus = pw.TextField(null=True)
    evidence_set = pw.TextField(null=True)
    attack_as_graph = pw.TextField(null=True)




class AuthorDetect(BaseModel):
    id = pw.IntegerField(null=False)
    author = pw.TextField(null=False)
    references = pw.TextField(null=False)
    num_papers = pw.IntegerField(null=False)
    total_citations = pw.IntegerField(null=False)
    max_citations = pw.IntegerField(null=False)
    min_citations = pw.IntegerField(null=False)
    coauthors = pw.TextField(null=False)

class Excluded_phase_b(BaseModel):
    id = pw.IntegerField(null=False)
    reference = pw.TextField(null=True)
    reason = pw.TextField(null=True)
    old_reason = pw.TextField(null=True)

class PossibleReferencesC2(BaseModel):
    id = pw.IntegerField(null=False)
    reference = pw.TextField(null=True)
    coming_from = pw.TextField(null=True)

class ReducedReferencesC2(BaseModel):
    id = pw.IntegerField(null=False)
    reference = pw.TextField(null=True)
    coming_from = pw.TextField(null=True)
    bibtex_id = pw.TextField(null=True)
    reference_string = pw.TextField(null=True)

class OrderedReferencesC2(BaseModel):
    id = pw.IntegerField(null=False)
    reference = pw.TextField(null=True)
    coming_from = pw.TextField(null=True)


if __name__== "__main__":
    try:
        Biblio.create_table()
    except pw.OperationalError:
        print "Biblio table already exists!"
