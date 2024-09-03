import pytest

from src.Category import Category
from src.iterators import CategoryIterator
from src.Product import Product


@pytest.fixture
def product_first():
    """фикстура на экземпляр класса Product."""
    return Product(
        name="NewBalance 530",
        description="оригинальные кроссовки",
        price=12390,
        quantity=10,
    )


@pytest.fixture
def product_second():
    """фикстура на экземпляр класса Product."""
    return Product(
        name="Iphone 15pro 1tb", description="iphone из китая", price=130000, quantity=6
    )


@pytest.fixture
def category1():
    """фикстура на экземпляр класса Category."""
    return Category(
        name="Одежда",
        description="стильная модная популярная",
        products=[
            Product("Футболка", "белая", 1100, 4),
            Product("Футболка", "черная", 900, 12),
            Product("NewBalance 990", "Кожа", 29689, 3),
        ],
    )


@pytest.fixture
def category2():
    """фикстура на экземпляр класса Category."""
    return Category(
        name="Электроника",
        description="Современная новая носимая электроника",
        products=[Product("iphone13", "green 256gb", 87900, 13)],
    )


@pytest.fixture
def data_test():
    """Фикстура для create_class."""
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "price": 210000.0,
                    "quantity": 8,
                },
                {
                    "name": "Xiaomi Redmi Note 11",
                    "description": "1024GB, Синий",
                    "price": 31000.0,
                    "quantity": 14,
                },
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром, шим другом и помощником",
            "products": [
                {
                    "name": '55" QLED 4K',
                    "description": "Фоновая подсветка",
                    "price": 123000.0,
                    "quantity": 7,
                }
            ],
        },
    ]


@pytest.fixture
def category_iterator1(category1):
    return CategoryIterator(category1)
