import pytest


def test_smartphone_init(smartphone1):
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.color == "Серый"
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256


def test_smartphones_add(smartphone1, smartphone2):
    assert smartphone1 + smartphone2 == 2580000.0


def test_smartphone_add_errors(smartphone1):
    with pytest.raises(TypeError):
        result = smartphone1 + 2
        return result
