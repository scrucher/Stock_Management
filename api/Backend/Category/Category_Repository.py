from ..Entity.Models import Category
from pony.orm import *


class CategoryRepository:
    def __init__(self):
        self.category = None

    @db_session
    def add(self, name: str):
        self.category = Category(name=name)
        commit()
        return self.category

    @db_session
    def get(self, category_id: int):
        return Category.get(id=category_id)

    @db_session
    def get_all(self):
        self.category = [s.to_dict() for s in Category.select()]
        return self.category

    @db_session
    def update(self, category_id: int, name: str):
        self.category = Category.get(id=category_id)
        if self.category:
            if name:
                self.category.name = name
                commit()
        return self.category

    @db_session
    def delete(self, category_id: int):
        self.category = Category.get(id=category_id)
        if self.category:
            Category.delete(id=category_id)
