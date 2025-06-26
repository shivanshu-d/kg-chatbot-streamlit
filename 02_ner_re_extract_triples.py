import spacy, pandas as pd

nlp = spacy.load("en_core_web_sm")

doc = nlp(open("D:\\Data Science\\knowledge-graph-chatbot\\data\\cleaned_user_agreement.txt", encoding="utf-8").read())

triples = []
for sent in doc.sents:
    ents = [ent.text for ent in sent.ents]
    if len(ents) >= 2:
        triples.append((ents[0], "related_to", ents[1]))

pd.DataFrame(triples, columns=["Entity1", "Relation", "Entity2"]).to_csv("D:\\Data Science\\knowledge-graph-chatbot\\triples\\extracted_triples.csv", index=False)
