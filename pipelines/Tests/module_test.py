"""Automatic tests for module"""
from pipelines import module

module = module()

def test_returns_int():
    assert module.returns_int() == 1
    assert isinstance(module.returns_int(), int)

def test_returns_str():
    assert module.returns_str() == "string"
    assert isinstance(module.returns_str(), str)

def test_returns_dict():
    dictionary = module.returns_dict()

    assert dictionary['key'] == "value"
    assert isinstance(module.returns_dict(), dict)

def test_returns_bool():
    assert module.returns_bool() is True
    assert isinstance(module.returns_bool(), bool)