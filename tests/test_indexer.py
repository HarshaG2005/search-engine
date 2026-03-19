import os
import sys

import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from core.indexer import build_bigram_index, build_index, get_bigrams
from core.preprocessor import preprocess
from core.storage import load_recipe


def test_build_index():
    recipes = load_recipe()
    index, doc_len, recipe_map, bigram_index = build_index(recipes)
    assert index is not None
    assert doc_len is not None
    assert recipe_map is not None
    assert bigram_index is not None
    assert index["garcinia"] is not None
    assert index["garcinia"][17] == {
      "tf": 1,
      "pos": [
        30
      ],
      "fields": {
        "title": 0,
        "ingredients": 1
      }
    }