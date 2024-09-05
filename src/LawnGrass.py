from src.Product import Product


class LawnGrass(Product):
    """Класс газонная трава унаследован от Product."""

    country: str
    germination_period: str
    color: str

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        """Инициация класса смартфоны добавляются новые атрибуты: производительность"""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """Метод сложения только для экземпляров класса LawnGrass"""
        if type(other) is LawnGrass:
            return self.quantity * self.price + other.quantity * other.price
        raise TypeError
