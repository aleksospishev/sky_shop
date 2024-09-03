import pytest


def test_categoryiterator(category_iterator1):
    assert category_iterator1.index == 0
    elem = next(category_iterator1)
    assert elem.name == "Футболка"
    assert elem.quantity == 4
    assert elem.price == 1100
    assert next(category_iterator1).name == "Футболка"
    assert category_iterator1.index == 2
    assert next(category_iterator1).name == "NewBalance 990"
    with pytest.raises(StopIteration):
        next(category_iterator1)
