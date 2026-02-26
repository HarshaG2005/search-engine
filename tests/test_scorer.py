import os
import sys

import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.indexer import indexes, recipes
from core.scorer import score


def test_scorer():
    from core.indexer import indexes, recipes
    from core.scorer import score

    # Test case 1: Basic relevance scoring
    query = "coconut"
    recipe=recipes[0]
    results = score(query,recipe, indexes, recipes)
    assert results > 0
    # Recipe ID 1 should be most relevant for "coconut milk"
    
    # Test case 2: Relevance scoring with multiple matches
    query = "prawn"
    recipe=recipes[1]
    results = score(query,recipe, indexes, recipes)
    assert results > 0
     # Recipe ID 2 should be most relevant for "prawn curry"
    
    # Test case 3: Relevance scoring with no matches
    query = "chocolate"
    recipe=recipes[0]
    results = score(query,recipe, indexes, recipes)
    assert results == 0  # No recipes should match "chocolate cake"