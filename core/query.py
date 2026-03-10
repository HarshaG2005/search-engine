import math
import os
import sys
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from core.preprocesser import preprocess
from core.spell_correct import spell_correct, bigram_index,transform
from storage import load


index, doc_len, avg_doc_len = load()

# weights
K1 = 1.5
B = 0.75
G_TITLE = 0.7
G_INGREDIENTS = 0.3

def bm25(tf, df, N, doc_len, avg_doc_len):
    idf = math.log(N / df)
    tf_score = ((K1 + 1) * tf) / (K1 * ((1 - B) + B * (doc_len / avg_doc_len)) + tf)
    return idf * tf_score

def field_boost(posting):
    return 1 + (G_TITLE * posting["fields"]["title"] + 
                G_INGREDIENTS * posting["fields"]["ingredients"])

def proximity(pos1, pos2):
    min_gap = float("inf")
    for p1 in pos1:
        for p2 in pos2:
            gap = abs(p1 - p2)
            if gap < min_gap:
                min_gap = gap
    return 1 / (1 + min_gap)

def proximity_boost(query_terms, doc_id):
    # only makes sense if query has more than one term
    if len(query_terms) < 2:
        return 1.0
    
    total = 0
    pairs = 0

    for i in range(len(query_terms)):
        for j in range(i + 1, len(query_terms)):
            t1 = query_terms[i]
            t2 = query_terms[j]

            # both terms must exist in this doc
            if t1 in index and doc_id in index[t1] and \
               t2 in index and doc_id in index[t2]:
                pos1 = index[t1][doc_id]["pos"]
                pos2 = index[t2][doc_id]["pos"]
                total += proximity(pos1, pos2)
                pairs += 1

    if pairs == 0:
        return 1.0
    
    # average proximity across all term pairs
    return 1 + (total / pairs)

def search(raw_query, top_k=5):
    query_terms = transform(raw_query)   # spell correct + preprocess
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
        scores[doc_id] *= proximity_boost(query_terms, doc_id)

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return ranked[:top_k]


if __name__ == "__main__":
    query = "stews"
    results = search(query)
    print(f"\nResults for '{query}':")
    for doc_id, score in results:
        print(f"  doc {doc_id} → score: {score:.4f}")
# ```

# ---

# **Why proximity is applied after the main loop:**
# ```
# BM25 + field → accumulated per term  (inside loop)
# proximity    → needs ALL terms done  (outside loop)