import os
import sys

import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from core.indexer import indexes, recipes
from core.scorer import score, search


def test_search():
    from core.indexer import indexes, recipes
    from core.scorer import search

    # Test case 1: Basic search functionality
    query = "coconut"
    results = search(query, recipes, indexes)
    assert len(results) > 0
    assert (
        results[0][0]["id"] == 1
    )  # Recipe ID 1 should be most relevant for "coconut milk"

    # Test case 2: Search with multiple matches
    query = "goraka"
    results = search(query, recipes, indexes)
    assert len(results) > 0
    assert results[0][0]["id"] == 5  #

    # Test case 3: Search with no matches
    query = "chocolate"
    results = search(query, recipes, indexes)
    assert len(results) == 0  # No recipes should match "chocolate cake"
