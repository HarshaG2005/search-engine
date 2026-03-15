import os
import sys

import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from search import search
from storage import load


def test_search():

    # Test case 1: Basic search
    results = search("chicken curry")
    assert len(results) > 0
    assert any("chicken" in r["title"].lower() for r in results)

    # Test case 2: Search with no results
    results = search("xyzabc")
    assert len(results) == 0

    # Test case 3: Search with multiple results
    results = search("beef stew")
    assert len(results) > 0
    assert any("beef stew" in r["title"].lower() for r in results)
    
    # Test case 4: Search with singlish query
    results = search("kukulmas cariya")
    assert len(results) > 0
    assert any("chicken curry" in r["title"].lower() for r in results)
