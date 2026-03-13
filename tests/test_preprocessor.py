import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest

from core.preprocessor import preprocess


def test_preprocessor():

    assert preprocess("Coconut Milk") == ["coconut", "milk"]
    assert preprocess("Spicy Prawn Curry") == ["spici", "prawn", "curri"]
