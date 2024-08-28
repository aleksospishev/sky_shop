from src.Product import Product


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
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self):
        """Геттер для списка продуктов в виде строки класса Category."""
        str_product = ""
        for product in self.__products:
            str_product += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return str_product

    @property
    def get_products_list_name(self):
        """Геттер для списка продуктов."""
        return self.__products

    def add_product(self, product: Product):
        """Метод для того чтобы добавить экземпляр класса Product в список продуктов."""
        self.__products.append(product)
        Category.product_count += 1
