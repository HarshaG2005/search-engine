from core.query import bm25, field_boost, format_results, proximity_boost
from core.spell_correct import transform
from storage import load

_index = None
_doc_len = None
_avg_doc_len = None
_recipe_map = None


def _ensure_loaded():
    global _index, _doc_len, _avg_doc_len, _recipe_map
    if _index is None:  # only loads if not already loaded
        _index, _doc_len, _avg_doc_len, _recipe_map = load()


def search(raw_query, top_k=5):
    _ensure_loaded()  # first call loads, all future calls skip

    query_terms = transform(raw_query, _index)
    N = len(_doc_len)
    scores = {}

    for term in query_terms:
        if term not in _index:
            continue
        df = len(_index[term])
        for doc_id, posting in _index[term].items():
            tf = posting["tf"]
            dl = _doc_len[doc_id]
            score = bm25(tf, df, N, dl, _avg_doc_len)
            score *= field_boost(posting)
            scores[doc_id] = scores.get(doc_id, 0) + score

    for doc_id in scores:
        scores[doc_id] *= proximity_boost(query_terms, doc_id, _index)

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return format_results(ranked, top_k, _recipe_map)
