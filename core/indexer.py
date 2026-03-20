import collections
import math

from core.preprocessor import preprocess


def get_bigrams(word):
    """Generate bigrams from a word."""
    word = word.lower()
    return [word[i : i + 2] for i in range(len(word) - 1)]


def build_bigram_index(indexes):
    """Builds a bigram index from the existing term index."""
    bigram_index = {}
    for word in indexes.keys():
        bigrams = get_bigrams(word)
        for bigram in bigrams:
            if bigram not in bigram_index:
                bigram_index[bigram] = []
            if word not in bigram_index[bigram]:
                bigram_index[bigram].append(word)
    return bigram_index


def build_index(recipes):
    """Builds an inverted index from the list of recipes."""
    # term -> doc_id -> stats
    index = collections.defaultdict(
        lambda: collections.defaultdict(
            lambda: {
                "tf": 0,
                "pos": [],
                "fields": {"title": 0, "ingredients": 0},
            }
        )
    )
    doc_len = {}  # doc_id -> total tokens indexed
    recipe_map = {}  # for easy lookup later

    for recipe in recipes:
        doc_id = recipe["id"]
        recipe_map[doc_id] = {
            "title": recipe.get("title", ""),
            "img_url": recipe.get("img_url", ""),
            "url": recipe.get("url", ""),
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
    bigram_index = build_bigram_index(index)
    return index, doc_len, recipe_map, bigram_index
