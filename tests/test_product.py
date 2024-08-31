from src.Product import Product


def test_product_init(product_first, product_second, category1):
    """Тест И нициализации экземпляра класса."""
    assert product_first.name == "NewBalance 530"
    assert product_first.description == "оригинальные кроссовки"
    assert product_first.price == 12390
    assert product_first.quantity == 9
    assert product_second.name == "Iphone 15pro 1tb"
    assert product_second.description == "iphone из китая"
    assert product_second.price == 139789
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
