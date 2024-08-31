import json
import os

from src.Category import Category
from src.Product import Product


def read_json_file(path: str) -> list[dict]:
    """Считывание из файла .Json"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def create_class_objects(data: list[dict]):
    """Создание экземпляров класса Category из списка полученного из Json."""
    categories = []
    for category in data:
        products = []
        for el in category["products"]:
            products.append(Product(**el))
        category["products"] = products
        categories.append(Category(**category))
    return categories
