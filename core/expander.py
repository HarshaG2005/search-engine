def expand(terms,thesaurus):
    expanded=[]
    for term in terms:
        expanded.append(term)
        expanded.extend(thesaurus.get(term,[]))
    return expanded
    