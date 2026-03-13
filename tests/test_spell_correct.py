import os
import sys

import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from nltk.metrics.distance import edit_distance

from core.preprocessor import preprocess
from core.spell_correct import (
    build_bigram_index,
    get_bigrams,
    get_candidates,
    spell_correct,
    transform,
)
from storage import load
indexes, doc_len, avg_doc_len, recipe_map = load()

def test_transform():
    assert transform('chikin curry',indexes) == ['chicken','curri']
    assert transform('lentil sup',indexes) == ['lentil','soup']
    assert transform('phish thacos',indexes) == ['fish','taco']