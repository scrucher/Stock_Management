from ..Entity.Models import Supplier
from pony.orm import *


class SupplierRepository:
    def __init__(self):
        self.supplier = None

    @db_session
    def add(self, data):
        self.supplier = Supplier(
                name=data['name'],
                location=data.get('location'),
                phone=data.get('phone'),
                email=data.get('email')
            )
        commit()
        return self.supplier

    @db_session
    def get(self, supplier_id: int):
        return Supplier.get(id=supplier_id)

    @db_session
    def get_all(self):
        self.supplier = [s.to_dict() for s in Supplier.select()]
        return self.supplier

    @db_session
    def update(self, supplier_id: int, data):
        self.supplier = Supplier.get(id=supplier_id)
        if self.supplier:
            if data:
                self.supplier.set(
                    name=data['name'],
                    location=data.get('location'),
                    phone=data.get('phone'),
                    email=data.get('email')
                )
                commit()
        return self.supplier

    @db_session
    def delete(self, supplier_id: int):
        self.supplier = Supplier.get(id=supplier_id)
        if self.supplier:
            Supplier.delete(id=supplier_id)
