from core.query import bm25, format_results, proximity_boost
from core.spell_correct import transform
from core.storage import load, load_thesaurus

_index = None
_doc_len = None
_avg_doc_len = None
_recipe_map = None
_bigram_index = None
_doc_field_len=None
_avg_field_len=None
_thesaurus = None


def _ensure_loaded():
    global _index, _doc_len, _avg_doc_len, _recipe_map, _bigram_index, _doc_field_len, _avg_field_len,_thesaurus
    if _index is None:  # only loads if not already loaded
        _index, _doc_len, _avg_doc_len, _recipe_map, _bigram_index, _doc_field_len, _avg_field_len = load()
        _thesaurus = load_thesaurus()


def search(raw_query, top_k=5):
    _ensure_loaded()  # first call loads, all future calls skip

    query_terms = transform(raw_query, _index, _bigram_index, _thesaurus)  # spell correct first
    N = len(_doc_len)
    scores = {}

    for term in query_terms:
        print('////////')
        print(f"Searching for term: '{term}' in Inverted Index")
        if term not in _index:
            continue
        df = len(_index[term])
        for doc_id, posting in _index[term].items():
            print(f"Calculating score for doc {doc_id} and term '{term}'")
            tf_title = posting["fields"]["title"]
            tf_ingr = posting["fields"]["ingredients"]
            title_len=_doc_field_len[doc_id]["title"]
            ingr_len=_doc_field_len[doc_id]["ingredients"]
            avg_title_len=_avg_field_len["title"]
            avg_ingr_len=_avg_field_len["ingredients"]
            dl = _doc_len[doc_id]
            #tf_title,tf_ingr,title_len,ingr_len, df, N, doc_len,avg_title_len,avg_ingr_len
            score = bm25(tf_title,tf_ingr,title_len,ingr_len, df, N, dl,avg_title_len=avg_title_len,avg_ingr_len=avg_ingr_len)
            # score *= field_boost(posting)
            scores[doc_id] = scores.get(doc_id, 0) + score

    for doc_id in scores:
        scores[doc_id] *= proximity_boost(query_terms, doc_id, _index)
    print(f'////////////')
    print(f"Scores of documents before ranking: {scores}")

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    print(f"Top {top_k} results: {ranked[:top_k]}\n")
    print('//////////')
    print(f"Final formatted results: {[ doc_id for doc_id,_ in ranked[:top_k]]}")
    return format_results(ranked, top_k, _recipe_map)
    