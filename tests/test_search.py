import pytest
def test_search():
    from core.scorer import search
    from core.indexer import indexes, recipes
    
    # Test case 1: Basic search functionality
    query = "coconut milk"
    results = search(query, recipes, indexes)
    assert len(results) > 0
    assert results[0][0]['id'] == 1  # Recipe ID 1 should be most relevant for "coconut milk"
    
    # Test case 2: Search with multiple matches
    query = "prawn curry"
    results = search(query, recipes, indexes)
    assert len(results) > 0
    assert results[0][0]['id'] == 2  # Recipe ID 2 should be most relevant for "prawn curry"
    
    # Test case 3: Search with no matches
    query = "chocolate cake"
    results = search(query, recipes, indexes)
    assert len(results) == 0  # No recipes should match "chocolate cake"