import os
import sys

import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from nltk.metrics.distance import edit_distance

from core.indexer import get_bigrams
from core.preprocessor import preprocess
from core.spell_correct import get_candidates, spell_correct, transform
from storage import load


def test_transform():
    indexes, doc_len, avg_doc_len, recipe_map, bigram_index = load()
    assert transform("chikin curry", indexes, bigram_index) == ["chicken", "curri"]
    assert transform("lentil sup", indexes, bigram_index) == ["lentil", "soup"]
    assert transform("phish thacos", indexes, bigram_index) == ["fish", "taco"]
