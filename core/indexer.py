import os
import sys
from nltk.stem import PorterStemmer
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import math
from core.preprocesser import preprocess
from data.recipes import recipes

ps = PorterStemmer()


def makeIndex(recipes):
    index = {}
    for recipe in recipes:
        content = (
            recipe["text"] + " " + recipe["title"]
        )  # to include the title in the search
        words = preprocess(content)
        for word in words:
            if word not in index:
                index[word] = []
            if recipe["id"] not in index[word]:
                index[word].append(recipe["id"])
    return index


indexes = makeIndex(recipes)


def search_2_words(word1, word2, indexes):
    word1 = word1.lower()  # to make the search case insensitive
    word2 = word2.lower()  # to make the search case insensitive
    word1 = ps.stem(word1)
    word2 = ps.stem(word2)
    ids1 = set(
        indexes.get(word1, [])
    )  # set(None) doesn't give an empty set — it crashes with a TypeError. set([]) gives an empty set. Small but important distinction to have right in your mental model.
    ids2 = set(indexes.get(word2, []))
    if ids1 and ids2:
        return list(ids1 & ids2)  # lists dont have intersection but sets do
    elif ids1:
        return list(ids1)
    elif ids2:
        return list(ids2)
    else:
        return None


if __name__ == "__main__":
    print(makeIndex(recipes))
