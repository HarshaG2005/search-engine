import collections
import json
import os
import math
from core.preprocesser import preprocess
with open(os.path.join(os.path.dirname(__file__), "../data/recipe.json")) as f:
    recipes = json.load(f)

def build_index(recipes):
    # term -> doc_id -> stats
    index = collections.defaultdict(lambda: collections.defaultdict(lambda: {
        "tf": 0,
        "pos": [],
        "fields": {"title": 0, "ingredients": 0},
    }))
    doc_len = {}  # doc_id -> total tokens indexed

    for recipe in recipes:
        doc_id = recipe["id"]

        title_tokens = preprocess(recipe.get("title", ""))
        ing_tokens = preprocess(" ".join(recipe.get("ingredients", [])))

        # We create one token stream so positions are consistent
        tokens = []
        tokens.extend(("title", t) for t in title_tokens)
        tokens.extend(("ingredients", t) for t in ing_tokens)

        doc_len[doc_id] = len(tokens)

        for position, (field, term) in enumerate(tokens):
            posting = index[term][doc_id]
            posting["tf"] += 1
            posting["pos"].append(position)
            posting["fields"][field] += 1

    return index, doc_len
indexes = build_index(recipes)

if __name__ == "__main__":
    print(indexes)