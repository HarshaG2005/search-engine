import collections
import math
from core.preprocesser import preprocess
def build_index(recipes):
    """Builds an inverted index from the list of recipes."""
    # term -> doc_id -> stats
    index = collections.defaultdict(lambda: collections.defaultdict(lambda: {
        "tf": 0,
        "pos": [],
        "fields": {"title": 0, "ingredients": 0},
    }))
    doc_len = {}  # doc_id -> total tokens indexed
    recipe_map = {r["id"]: r for r in recipes}  # for easy lookup later

    for recipe in recipes:
        doc_id = recipe["id"]
        recipe_map[doc_id] = {
            "title": recipe.get("title", ""),
            "ingredients": recipe.get("ingredients", []),
        }

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

    return index, doc_len,recipe_map

