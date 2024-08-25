class Product:
    """Класс описывающий товары."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализация экземпляров класса Product."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


if __name__ == "__main__":
    product = Product("кросоки", "Nike", 3500, 5)
    print(product.name)
    print(product.quantity)
