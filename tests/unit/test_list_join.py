import pytest
from src.generator import list_join


def test_list_join():
    connectors = [1,2]
    list_ = ["a","b", "c"]
    assert list_join(connectors, list_) == ["a", 1, "b", 2, "c"]

def test_list_join_same_length():
    connectors = [1,2,3]
    list_ = ["a","b", "c"]
    assert list_join(connectors, list_) == ["a", 1, "b", 2, "c"]

def test_list_join_connectors_too_small():
    connectors = [1]
    list_ = ["a","b", "c"]
    with pytest.raises(ValueError):
        list_join(connectors, list_)
    connectors = []
    list_ = ["a","b"]
    with pytest.raises(ValueError):
        list_join(connectors, list_)

def test_list_join_one_element():
    connectors = []
    list_ = ["a"]
    assert list_join(connectors, list_) == ["a"]
    connectors = [1]
    list_ = ["a"]
    assert list_join(connectors, list_) == ["a"]

