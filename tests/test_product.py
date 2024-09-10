import pytest

from src.Product import Product


def test_product_init(product_first, product_second, category1):
    """Тест И нициализации экземпляра класса."""
    assert product_first.name == "NewBalance 530"
    assert product_first.description == "оригинальные кроссовки"
    assert product_first.price == 12390
    assert product_first.quantity == 10
    assert product_second.name == "Iphone 15pro 1tb"
    assert product_second.description == "iphone из китая"
    assert product_second.price == 130000
    assert product_second.quantity == 6
    new_product = Product.new_product(
        {
            "name": "Xiaomi Redmi Note 11",
            "description": "1024GB, Синий",
            "price": 31000.0,
            "quantity": 14,
        }
    )
    assert new_product.name == "Xiaomi Redmi Note 11"
    new_product.price = 32000.0
    assert new_product.price == 32000
    new_product.price = -4
    assert new_product.price == 32000
    new_product_2 = Product.new_product(
        {"name": "Футболка", "descriptions": "белая", "price": 1000, "quantity": 2},
        category1.get_products_list_name,
    )
    assert new_product_2.name == "Футболка"
    assert new_product_2.quantity == 6
    assert new_product_2.price == 1100
    new_product_3 = Product.new_product(
        {"name": "Футболка", "description": "белая", "price": 1400, "quantity": 2},
        category1.get_products_list_name,
    )
    assert new_product_3.price == 1400
    new_product4 = Product.new_product(
        {"name": "шорты", "description": "черные", "price": 1400, "quantity": 2},
        category1.get_products_list_name,
    )
    assert new_product4.name == "шорты"


def test_new_method_product(product_first, product_second):
    assert str(product_first) == "NewBalance 530, 12390 руб. Остаток: 10 шт."
    assert str(product_second) == "Iphone 15pro 1tb, 130000 руб. Остаток: 6 шт."
    assert product_first + product_second == 903900


def test_init_product_not_validle():
    with pytest.raises(ValueError):
        product1 = Product("Футболка", "белая", 1000, 0)
        return product1

