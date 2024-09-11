import pytest


def test_category_init(category1, category2):
    """Тест класса Category."""
    assert category1.name == "Одежда"
    assert category1.description == "стильная модная популярная"
    assert category2.name == "Электроника"
    assert category2.description == "Современная новая носимая электроника"
    assert category1.product_count == 4
    assert category1.category_count == 2


def test_category_setter(category1, product_first):
    assert len(category1.get_products_list_name) == 3
    category1.add_product(product_first)
    assert len(category1.get_products_list_name) == 4


def test_new_method_category(category1, category2):
    assert str(category1) == "Одежда, количество продуктов: 19 шт."
    assert str(category2) == "Электроника, количество продуктов: 13 шт."


def test_category_setter_error(category1):
    with pytest.raises(TypeError):
        category1.add_product("product_first")


def test_middle_price(category1, category2, category3):
    assert category1.middle_price() == 10563.0
    assert category2.middle_price() == 87900.0
    assert category3.middle_price() == 0
