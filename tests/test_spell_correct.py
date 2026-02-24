import pytest
def test_spell_correct():
    from core.spell_correct import spell_correct
    from core.indexer import indexes
    from core.preprocesser import preprocess
    
    # Test case 1: Basic correction
    assert spell_correct("cocnut", indexes, indexes) == "coconut"
    
    # Test case 2: Correction with multiple candidates
    assert spell_correct("prwan", indexes, indexes) == "prawn"
    
    # Test case 3: No correction needed
    assert spell_correct("spicy", indexes, indexes) == "spici"  # "spicy" is not in the index, but "spici" is the stemmed form that matches
    
    # Test case 4: No valid correction
    assert spell_correct("xyzabc", indexes, indexes) == "xyzabc"  # No close match, should return original query