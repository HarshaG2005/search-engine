import os
import sys
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from core.indexer import build_index
from storage import load_recipe
from core.preprocessor import preprocess
recipes = load_recipe()

def test_build_index():

    index,doc_len,recipe_map = build_index(recipes)
    assert index is not None
    assert doc_len is not None
    assert recipe_map is not None
    assert index["chicken"] is not None
    assert index["chicken"][12]=={
      "tf": 2,
      "pos": [
        0,
        2
      ],
      "fields": {
        "title": 1,
        "ingredients": 1
      }
    }
    