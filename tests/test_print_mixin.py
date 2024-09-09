from src.LawnGrass import LawnGrass
from src.Product import Product
from src.Smartphone import Smartphone


def test_mixin(capsys):
    Product("NewBalance 530", "оригинальные кроссовки", 12390, 10)
    message = capsys.readouterr()
    assert (
        message.out.strip()
        == "Product(NewBalance 530, оригинальные кроссовки, 12390, 10)"
    )

    Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )
    message = capsys.readouterr()
    assert (
        message.out.strip()
        == "Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"
    )

    LawnGrass(
        "Газонная трава",
        "Элитная трава трава газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
    message = capsys.readouterr()
    assert (
        message.out.strip()
        == "LawnGrass(Газонная трава, Элитная трава трава газона, 500.0, 20)"
    )
