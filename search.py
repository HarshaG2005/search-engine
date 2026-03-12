import math
import os
import sys
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from core.preprocesser import preprocess
from core.spell_correct import spell_correct,transform
from storage import load
from core.query import bm25, field_boost, proximity_boost, format_results


index, doc_len, avg_doc_len, recipe_map = load()

def search(raw_query, top_k=5):
    query_terms = transform(raw_query,index)   # spell correct + preprocess
    N = len(doc_len)
    scores = {}

    for term in query_terms:
        if term not in index:
            continue
        df = len(index[term])

        for doc_id, posting in index[term].items():
            tf = posting["tf"]
            dl = doc_len[doc_id]

            score = bm25(tf, df, N, dl, avg_doc_len)
            score *= field_boost(posting)

            scores[doc_id] = scores.get(doc_id, 0) + score

    # apply proximity boost after accumulating BM25 + field scores
    for doc_id in scores:
        scores[doc_id] *= proximity_boost(query_terms, doc_id, index)

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return format_results(ranked, top_k, recipe_map)
print(search("chiken cocnut curi", top_k=3))
