<<<<<<< HEAD
# sky_shop
Интернет магазин Sky_Shop 
Проект нацелен на обучению и отработке навыков ООП. 
проект построен на двух родительских классах:
Класс Product имеющий атрибуты:
    -имя (name)
    -описание (description)
    -цена (price)
    -количетсво (quantity)
и класс Category 
    -имя (name)
    -описание (description)
    -список продуктов в жтой категории (products)
    -количество экземпляров класса (category_count)
    -количесво товаров в классе (product_count)
от класса Product наследованы два класса с дополнеными атрибутами:
класс Smartphones:
    -эффективность (efficiency)
    -модель (model)
    -объем памяти (memory)
    -цвет (color),
а также класс LawnGrassЖ
    -страна (country)
    -период взвращивания (germination_period)
    -цветт (color)
На все методы классов написаны тесты в модуле tests.
Покрытие кода тестами составляет 87%


## Технологии
- [Python 3.12]
- [ООП]
- [Poetry]
- [Pytest]
- [JSON]

## Установка 

1. Клонируйте репозиторий:
```
git clone https://github.com/aleksospishev/sky_shop.git
```

2. Установите зависимости:
```
poetry install
```
3. Запуск тестов:
```
poetry pytest
```
4. Проверить покрытие кода тестами
```
poetry run pytest --cov
```

