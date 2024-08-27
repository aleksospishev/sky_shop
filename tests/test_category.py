def test_category_init(category1, category2):
    """Тест класса Category."""
    assert category1.name == "Одежда"
    assert category1.description == "стильная модная популярная"
    assert category2.name == "Электроника"
    assert category2.description == "Современная новая носимая электроника"
    assert category2.product_count == 4
    assert category1.category_count == 2
