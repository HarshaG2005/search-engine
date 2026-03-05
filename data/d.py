import json
import os
import sys 
import collections
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from core.indexer import build_index
from core.preprocesser import preprocess
from storage import save, load

with open(os.path.join(os.path.dirname(__file__), "recipe.json")) as f:
     recipes = json.load(f)
def run_index():
    indexes, doc_len = build_index(recipes)
    avg_doc_len = sum(doc_len.values()) / len(doc_len) if doc_len else 0
    save(indexes, doc_len, avg_doc_len)
# # recipe = recipes["12"]
# # print(recipe["title"] + " " + " ".join(recipe["ingredients"]))
# for recipe in recipes:
#     print(recipe["title"])

# # from collections import defaultdict
# # index=defaultdict(set)
# # index["coconut"]=[1,2]
# # index["coconu"].add(3)
# # print(index)
# from storage import save, load
# index, doc_len, avg_doc_len = load()

# print(doc_len)
# print(avg_doc_len)
