from src.Product import Product
from src.zeroproducterror import ZeroProductError


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

    def __repr__(self):
        return (
            f"{self.__class__.name}: {self.name}, {self.description}, {self.__products}"
        )

    def __str__(self):
        count_product = 0
        for product in self.__products:
            count_product += product.quantity
        return f"{self.name}, количество продуктов: {count_product} шт."

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
        if isinstance(product, Product):
            try:
                if product.quantity <= 0:
                    raise ZeroProductError(
                        "количество товара не может быть нулевым или отрицательным"
                    )
            except ZeroProductError as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print("добавление товара прошло успешно")
            finally:
                print("обработка добавления товара завершена")
        else:
            raise TypeError

    def middle_price(self):
        try:
            return round(
                sum([product.price for product in self.__products])
                / len(self.__products),
                2,
            )
        except ZeroDivisionError:
            return 0.0
