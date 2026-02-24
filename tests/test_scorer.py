import pytest
def test_scorer():
    from core.scorer import score
    from core.indexer import indexes, recipes
    
    # Test case 1: Basic relevance scoring
    query = "coconut milk"
    results = score(query, indexes, recipes)
    assert len(results) > 0
    assert results[0][0] == 1  # Recipe ID 1 should be most relevant for "coconut milk"
    
    # Test case 2: Relevance scoring with multiple matches
    query = "prawn curry"
    results = score(query, indexes, recipes)
    assert len(results) > 0
    assert results[0][0] == 2  # Recipe ID 2 should be most relevant for "prawn curry"
    
    # Test case 3: Relevance scoring with no matches
    query = "chocolate cake"
    results = score(query, indexes, recipes)
    assert len(results) == 0  # No recipes should match "chocolate cake"