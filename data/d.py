# import json
# import os

# with open(os.path.join(os.path.dirname(__file__), "dt.json")) as f:
#     recipes = json.load(f)

# # recipe = recipes["12"]
# # print(recipe["title"] + " " + " ".join(recipe["ingredients"]))
# for recipe in recipes:
#     print(recipe["title"])

# # from collections import defaultdict
# # index=defaultdict(set)
# # index["coconut"]=[1,2]
# # index["coconu"].add(3)
# # print(index)
from storage import save, load
index, doc_len, avg_doc_len = load()

print(doc_len)
print(avg_doc_len)