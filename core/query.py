import math

K1 = 1.2
B_TITLE = 0.5      # less length normalization for short titles
B_INGR  = 0.75
W_TITLE = 3.0      # title is more important
W_INGR  = 1.0
# def bm25(tf_title,tf_ingr,title_len,ingr_len, df, N, doc_len,avg_title_len,avg_ingr_len):
#     idf = math.log((N - df + 0.5) / (df + 0.5) + 1)
#     # tf_score = ((K1 + 1) * tf) / (K1 * ((1 - B) + B * (doc_len / avg_doc_len)) + tf)
#     tf = (3.0 * tf_title)   / ((1 - 0.5)  + 0.5  *(title_len   / avg_title_len))+ (1.0 * tf_ingr)    / ((1 - 0.75) + 0.75 * (ingr_len    / avg_ingr_len))
#     return idf * tf
def bm25(tf_title, tf_ingr, title_len, ingr_len,df,N,doc_len, avg_title_len, avg_ingr_len):
    idf = math.log((N - df + 0.5) / (df + 0.5) + 1)
    # BM25F: normalize each field's tf separately, then apply weight
    # normalized tf per field
    tf_title_norm = tf_title / ((1 - B_TITLE) + B_TITLE * (title_len / avg_title_len))
    tf_ingr_norm  = tf_ingr  / ((1 - B_INGR)  + B_INGR  * (ingr_len  / avg_ingr_len))

    # weighted combination
    pseudo_tf = W_TITLE * tf_title_norm + W_INGR * tf_ingr_norm

    # final BM25 saturation
    tf_score = ((K1 + 1) * pseudo_tf) / (K1 + pseudo_tf)

    return idf * tf_score

# def field_boost(posting):
#     return 1 + (
#         G_TITLE * posting["fields"]["title"]
#         + G_INGREDIENTS * posting["fields"]["ingredients"]
#     )


def proximity(pos1, pos2):
    min_gap = float("inf")
    for p1 in pos1:
        for p2 in pos2:
            gap = abs(p1 - p2)
            if gap < min_gap:
                min_gap = gap
    return 1 / (1 + min_gap)


def proximity_boost(query_terms, doc_id, index):
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
            if (
                t1 in index
                and doc_id in index[t1]
                and t2 in index
                and doc_id in index[t2]
            ):
                pos1 = index[t1][doc_id]["pos"]
                pos2 = index[t2][doc_id]["pos"]
                total += proximity(pos1, pos2)
                pairs += 1

    if pairs == 0:
        return 1.0

    # average proximity across all term pairs
    return 1 + (total / pairs)


def format_results(ranked, top_k=5, recipe_map=None):
    results = []
    for doc_id, score in ranked[:top_k]:
        recipe = recipe_map.get(doc_id)
        results.append({"title": recipe["title"], "score": round(score, 4), "img_url": recipe.get("img_url", ""), "url": recipe.get("url", "")})
    return results
