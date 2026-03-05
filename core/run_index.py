import json
import os
import sys
import collections
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from core.indexer import build_index
from core.preprocesser import preprocess
with open(os.path.join(os.path.dirname(__file__), "../data/recipe.json")) as f:
    recipes = json.load(f)



def run_index():

