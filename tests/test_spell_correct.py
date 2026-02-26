import os
import sys

import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from nltk.metrics.distance import edit_distance

from core.indexer import indexes
from core.preprocesser import preprocess
from core.spell_correct import (build_bigram_index, get_bigrams,
                                get_candidates, spell_correct)
bigram_index=build_bigram_index(indexes)


def test_spell_correct():
    # Test case 1: Basic correction
    assert spell_correct('cocnut', bigram_index, indexes, threshold=2) == "coconut"
    
    # Test case 2: Correction with multiple candidates
    assert spell_correct('prwan', bigram_index, indexes, threshold=2) == "prawn"
    
    # Test case 3: No correction needed
    assert spell_correct('spic', bigram_index, indexes, threshold=2) == "spici"  # "spicy" is not in the index, but "spici" is the stemmed form that matches
    
    # Test case 4: No valid correction
    assert spell_correct('xyzabc', bigram_index, indexes, threshold=2) == "xyzabc"  # No close match, should return original query