# import json
# import os

# with open(os.path.join(os.path.dirname(__file__), "dt.json")) as f:
#     recipes = json.load(f)

# # recipe = recipes["12"]
# # print(recipe["title"] + " " + " ".join(recipe["ingredients"]))
# print(list(recipes.values())[0]["title"] + " " + " ".join(list(recipes.values())[0]["ingredients"]))

# from collections import defaultdict
# index=defaultdict(set)
# index["coconut"]=[1,2]
# index["coconu"].add(3)
# print(index)