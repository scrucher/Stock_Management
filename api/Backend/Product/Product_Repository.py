from ..Entity.Models import Product
from pony.orm import *


class ProductRepository:
    def __init__(self):
        self.product = None

    @db_session
    def add(self, data):
        self.product = Product(
            name=data['name'],
            image_name=data['image_name'],
            category=data['category'],
            expiration_date=data['expiration_date'],
            unit_price=data['unit_price'],
            unit=data['unit']
        )
        commit()
        return self.product

    @db_session
    def get(self, product_id: int):
        query = select(
            (p, c, u)
            for p in Product
            for c in JOIN(p.category)
            for u in JOIN(p.unit)
        ).where(id=product_id)
        product_dicts = [
            {
                'id': p.id,
                'name': p.name,
                'unit_price': p.unit_price,
                'expiration_date': p.expiration_date,
                'category': c.name,
                'unit': u.name
            }
            for p, c, u in query
        ]
        return product_dicts

    @db_session
    def get_all(self):
        self.product = select(
            (p, c, u)
            for p in Product
            for c in JOIN(p.category)
            for u in JOIN(p.unit)
        )
        product_dicts = [
            {
                'id': p.id,
                'name': p.name,
                'unit_price': p.unit_price,
                'expiration_date': p.expiration_date,
                'category': c.name,
                'unit': u.name
            }
            for p, c, u in self.product
        ]

        return product_dicts


@db_session
def update(self, product_id: int, data):
    self.product = Product.get(id=product_id)
    if self.product:
        if data:
            self.product.set(
                name=data['name'],
                image_name=data['image_name'],
                category=data['category_id'],
                expiration_date=data['expiration_date'],
                unit_price=data['unit_price'],
                unit_id=data['unit_id']
            )
            commit()
    return self.product


@db_session
def delete(self, product_id: int):
    self.product = Product.get(id=product_id)
    if self.product:
        Product.delete(id=product_id)
