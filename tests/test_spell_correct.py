import os
import sys

import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from nltk.metrics.distance import edit_distance

from core.indexer import get_bigrams
from core.preprocessor import preprocess
from core.spell_correct import get_candidates, spell_correct, transform
from core.storage import load, load_thesaurus
from core.expander import expand


def test_transform():
    indexes, doc_len, avg_doc_len, recipe_map, bigram_index = load()
    thesaurus = load_thesaurus()
    assert transform("chicen curry", indexes, bigram_index,thesaurus) == ["chicken", "curri"]
    assert transform("pani dadol", indexes, bigram_index,thesaurus) == ["pani", "dadol"]
    assert transform("malu", indexes, bigram_index,thesaurus) == [ "malu", "fish"]
    assert transform("kukulmas", indexes, bigram_index,thesaurus) == ["kukulma","chicken"]