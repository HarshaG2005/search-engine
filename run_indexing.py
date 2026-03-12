import json
import os
import sys
import collections
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from core.indexer import build_index
from core.preprocesser import preprocess
from storage import save,load_recipe
recipes = load_recipe()


def run_indexing():
    indexes,doc_len,recipe_map = build_index(recipes)
    avg_doc_len = sum(doc_len.values()) / len(doc_len) if doc_len else 0
    save(indexes, doc_len, avg_doc_len, recipe_map)
    return True
    
if __name__ == "__main__":
    run_indexing()
    print("Indexing completed successfully.")