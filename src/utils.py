import json
import os
from src.Product import Product
from src.Category import Category


def read_json_file(path: str) -> list[dict]:
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def create_clacc_objects(data: list[dict]):
    categories = []
    for category in data:
        products = []
        for el in category['products']:
            products.append(Product(**el))
        category['products'] = products
        categories.append(Category(**category))
    return categories

