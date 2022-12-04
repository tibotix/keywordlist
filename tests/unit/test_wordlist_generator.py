import pytest
from src import WordlistGenerator


def test_default_options():
    assert len(WordlistGenerator({}).generate()) == 0

def test_unique_keywords():
    options = {
        "keywords": ("kw1","kw1"),
        "max_keyword_conjunctions": 2
    }
    builder = WordlistGenerator(options)
    wordlist = builder.generate()
    assert wordlist.count("kw1kw1") == 2

def test_unique():
    options = {
        "keywords": ("kw1","Kw1"),
        "modifiers": (lambda x:x, lambda x:x.lower()),
        "max_keyword_conjunctions": 2
    }
    builder = WordlistGenerator(options)
    wordlist = builder.generate(unique=True)
    assert wordlist.count("kw1kw1") == 1
    wordlist = builder.generate(unique=False)
    assert wordlist.count("kw1kw1") == 4
