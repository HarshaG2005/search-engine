import os
import sys
import json
import collections
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import math
from core.preprocesser import preprocess

with open(os.path.join(os.path.dirname(__file__), "../data/recipe.json")) as f:
    recipes = json.load(f)

def makeIndex(recipes):
    index = collections.defaultdict(set)
    for recipe in recipes.values():
        content = recipe["title"] + " " + " ".join(recipe["ingredients"])
        words = preprocess(content)
        for word in words:
           index[word].add(recipe["id"])
    return index

indexes = makeIndex(recipes)

if __name__ == "__main__":
    print(makeIndex(recipes))
