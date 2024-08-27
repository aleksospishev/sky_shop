import pytest

from src.Category import Category
from src.Product import Product


@pytest.fixture
def product_first():
    """фикстура на экземпляр класса Product."""
    return Product(name="NewBalance 530", description="оригинальные кроссовки", price=12390, quantity=9)


@pytest.fixture
def product_second():
    """фикстура на экземпляр класса Product."""
    return Product(name="Iphone 15pro 1tb", description="iphone из китая", price=139789, quantity=6)


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
