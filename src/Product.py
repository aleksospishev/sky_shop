# from src.Category import Category

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
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, params_dict: dict, products_list=None):
        """Класс-метод для добавления новых экземпляров классаб из словаря."""
        if not products_list or products_list == []:
            return cls(**params_dict)
        for product in products_list:
            if params_dict['name'] == product.name:
                product.quantity += params_dict['quantity']
                if params_dict['price'] > product.price:
                    product.price = params_dict['price']
                return product
            else:
                return cls(**params_dict)

    @property
    def price(self):
        """Геттер для параметра цена проддукта."""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для изменения цены у товара, при попытке снижения цены требуется подтверждение"""
        if new_price > 0:
            if self.__price > new_price:
                answer = input('Вы действительно хотите снизить цену?(y/n)\n')
                if answer.lower() == 'y':
                    self.__price = new_price
            else:
                self.__price = new_price
        else:
            print('Цена не должна быть нулевая или отрицательная')
            return


if __name__ == "__main__":
    product = Product("кросовки", "Nike", 3500, 5)
    print(product.name)
    print(product.quantity)
