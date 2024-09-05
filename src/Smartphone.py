from src.Product import Product


class Smartphone(Product):
    """Класс смартфоны унаследован от Product."""

    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        """Инициация класса смартфоны добавляются новые атрибуты: производительность"""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """Метод сложения только для экземпляров класса Smartphones"""
        if type(other) is Smartphone:
            return self.quantity * self.price + other.quantity * other.price
        raise TypeError

    # @property
    # def price(self):
    #     """Геттер для параметра цена проддукта."""
    #     return self.__price
