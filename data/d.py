import json
import os

with open(os.path.join(os.path.dirname(__file__), "recipe.json")) as f:
    recipes = json.load(f)

print(recipes.values())