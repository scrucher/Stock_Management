from ..Entity.Models import OutboundStock, Stock
from pony.orm import *


class OutboundStockRepository:
    def __init__(self):
        self.out_stock = None

    @db_session
    def add(self, data):
        # required_fields = ['quantity', 'product_id', 'supplier_id', 'unit_price', 'user_id', 'tva_rate', 'invoice']
        # for field in required_fields:
        #     if field not in data:
        #         return jsonify({'error': f'{field} is required'}), 400
        stock = Stock.get(product_id=data['product_id'])
        if stock:
            stock.current_stock -= data['quantity']
            self.out_stock = OutboundStock(
                quantity=data['quantity'],
                product_id=data['product_id'],
                date_out=data['date_out'],
                user_id=data['user_id'],
                unit_price=data['unit_price'],
                client_id=data['supplier_id'],
                invoice=data['invoice'],
            )
            commit()
            return self.out_stock
        else:
            try:
                Stock(
                    quantity=data['quantity'],
                    product_id=data['product_id'],
                    date_out=data['date_out'],
                    user_id=data['user_id'],
                    unit_price=data['unit_price'],
                    client_id=data['supplier_id'],
                    invoice=data['invoice'],
                )
                self.out_stock = OutboundStock(
                    quantity=data['quantity'],
                    product_id=data['product_id'],
                    date_out=data['date_out'],
                    user_id=data['user_id'],
                    unit_price=data['unit_price'],
                    client_id=data['supplier_id'],
                    invoice=data['invoice'],
                )
                commit()
                return self.out_stock
            except Exception as e:
                return e




@db_session
def get(self, out_stock_id: int):
    return OutboundStock.get(id=out_stock_id)


@db_session
def get_all(self):
    self.out_stock = [s.to_dict() for s in OutboundStock.select()]
    return self.out_stock


@db_session
def update(self, out_stock_id: int, name: str):
    self.out_stock = OutboundStock.get(id=out_stock_id)
    if self.out_stock:
        if name:
            self.out_stock.name = name
            commit()
    return self.out_stock


@db_session
def delete(self, out_stock_id: int):
    self.out_stock = OutboundStock.get(id=out_stock_id)
    if self.out_stock:
        OutboundStock.delete(id=out_stock_id)
