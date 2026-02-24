import os
import sys

import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.indexer import makeIndex, recipes
from core.preprocesser import preprocess


def test_make_index():
    
    index = makeIndex(recipes)
    assert 'coconut' in index
    assert 1 in index['coconut']
    assert 2 in index['coconut']
    assert 3 in index['coconut']

