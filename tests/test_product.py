def test_product_init(product_first, product_second):
    """Тест И нициализации экземпляра класса."""
    assert product_first.name == "NewBalance 530"
    assert product_first.description == "оригинальные кроссовки"
    assert product_first.price == 12390
    assert product_first.quantity == 9
    assert product_second.name == "Iphone 15pro 1tb"
    assert product_second.description == "iphone из китая"
    assert product_second.price == 139789
    assert product_second.quantity == 6
