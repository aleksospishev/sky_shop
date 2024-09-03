class CategoryIterator:
    def __init__(self, object_category):
        self.category = object_category
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.category.get_products_list_name):
            product = self.category.get_products_list_name[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
