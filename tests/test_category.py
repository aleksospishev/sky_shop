def test_category_init(category1, category2, product_first):
    """Тест класса Category."""
    assert category1.name == "Одежда"
    assert category1.description == "стильная модная популярная"
    assert category2.name == "Электроника"
    assert category2.description == "Современная новая носимая электроника"
    assert category2.product_count == 4
    assert category1.category_count == 2
    prod_1 = "Футболка, 1100 руб. Остаток: 4 шт.\n"
    prod_2 = "Футболка, 900 руб. Остаток: 12 шт.\n"
    assert (
        category1.products
        == f"{prod_1}{prod_2}NewBalance 990, 29689 руб. Остаток: 3 шт.\n"
    )
    assert len(category1.get_products_list_name) == 3
    category1.add_product(product_first)
    assert category1.product_count == 5


def test_new_method_category(category1, category2):
    assert str(category1) == "Одежда, количество продуктов: 19 шт."
    assert str(category2) == "Электроника, количество продуктов: 13 шт."
