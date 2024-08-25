class Category:
    """Класс описывающий категории товаров и включает в себя список экземпляров класса Product."""

    name: str
    description: str
    products: list[dict]
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Инициализация экземпляров класса Category."""
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)
