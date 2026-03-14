# core/expander.py
from core.preprocessor import preprocess

def expand(terms, thesaurus):
    expanded = []
    for term in terms:
        expanded.append(term)
        synonyms = thesaurus.get(term, [])
        for synonym in synonyms:
            stemmed = preprocess(synonym)   # stem the expanded term
            expanded.extend(stemmed)
    return expanded