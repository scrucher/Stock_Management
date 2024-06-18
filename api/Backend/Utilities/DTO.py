from typing import Optional, Tuple, Union
from flask import Response


class CategoryDTO:
    def __init__(self,
                 name: str):
        self.name = name


class SupplierDTO:
    def __init__(self,
                 name: str,
                 location: Optional[str] = None,
                 phone: Optional[str] = None,
                 email: Optional[str] = None):
        self.name = name
        self.location = location
        self.phone = phone
        self.email = email


class ClientDTO:
    def __init__(self,
                 name: str,
                 contact: Optional[str] = None,
                 email: Optional[str] = None):
        self.name = name
        self.contact = contact
        self.email = email


class ServiceDTO:
    def __init__(self,
                 name: str):
        self.name = name


class UserDTO:
    def __init__(self,
                 username: str,
                 password: str,
                 role: str,
                 name: Optional[str] = None,
                 cin: Optional[str] = None,
                 email: Optional[str] = None,
                 phone: Optional[str] = None,
                 service_id: Optional[int] = None):
        self.username = username
        self.password = password
        self.role = role
        self.name = name
        self.cin = cin
        self.email = email
        self.phone = phone
        self.service_id = service_id


class ProductDTO:
    def __init__(self,
                 name: str,
                 image_name: Optional[str] = None,
                 category_id: Optional[int] = None,
                 expiration_date: Optional[str] = None,
                 modification_date: Optional[str] = None,
                 registration_date: Optional[str] = None,
                 unit_price: Optional[float] = None,
                 unit_id: Optional[int] = None):
        self.name = name
        self.image_name = image_name
        self.category_id = category_id
        self.expiration_date = expiration_date
        self.modification_date = modification_date
        self.registration_date = registration_date
        self.unit_price = unit_price
        self.unit_id = unit_id


class UnitDTO:
    def __init__(self,
                 name: str):
        self.name = name


class StockDTO:
    def __init__(self,
                 product_id: int,
                 stock_security: int,
                 stock_max: int,
                 unit_price: float,
                 current_stock: float):
        self.product_id = product_id
        self.stock_security = stock_security
        self.stock_max = stock_max
        self.unit_price = unit_price
        self.current_stock = current_stock


class InboundStockDTO:
    def __init__(self,
                 quantity: int,
                 product_id: int,
                 date_in: str,
                 supplier_id: int,
                 unit_price: float,
                 user_id: int,
                 tva_rate: Optional[float] = None,
                 invoice: Optional[str] = None):
        self.quantity = quantity
        self.product_id = product_id
        self.date_in = date_in
        self.supplier_id = supplier_id
        self.unit_price = unit_price
        self.user_id = user_id
        self.tva_rate = tva_rate
        self.invoice = invoice


class OutboundStockDTO:
    def __init__(self,
                 quantity: int,
                 product_id: int,
                 date_out: str,
                 user_id: int,
                 unit_price: float,
                 client_id: Optional[int] = None):
        self.quantity = quantity
        self.product_id = product_id
        self.date_out = date_out
        self.user_id = user_id
        self.unit_price = unit_price
        self.client_id = client_id


class ProductClientDTO:
    def __init__(self,
                 client_id: int,
                 product_id: int):
        self.client_id = client_id
        self.product_id = product_id


class ProductSupplierDTO:
    def __init__(self,
                 supplier_id: int,
                 product_id: int):
        self.supplier_id = supplier_id
        self.product_id = product_id


class CategorySupplierDTO:
    def __init__(self,
                 category_id: int,
                 supplier_id: int):
        self.category_id = category_id
        self.supplier_id = supplier_id


class InventoryAuditDTO:
    def __init__(self,
                 product_id: int,
                 user_id: int,
                 audit_date: str,
                 audit_quantity: int,
                 audit_id_uniq: int,
                 notes: Optional[str] = None):
        self.product_id = product_id
        self.user_id = user_id
        self.audit_date = audit_date
        self.audit_quantity = audit_quantity
        self.audit_id_uniq = audit_id_uniq
        self.notes = notes


class OrdersDTO:
    def __init__(self,
                 order_date: str,
                 client_id: int,
                 total_amount: float,
                 status: str):
        self.order_date = order_date
        self.client_id = client_id
        self.total_amount = total_amount
        self.status = status


class OrderItemsDTO:
    def __init__(self,
                 order_id: int,
                 product_id: int,
                 quantity: int,
                 unit_price: float):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.unit_price = unit_price


class DeliveriesDTO:
    def __init__(self,
                 order_id: int,
                 delivery_date: str,
                 delivered_by: int,
                 status: str):
        self.order_id = order_id
        self.delivery_date = delivery_date
        self.delivered_by = delivered_by
        self.status = status


class ReturnsDTO:
    def __init__(self,
                 order_id: int,
                 return_date: str,
                 product_id: int,
                 quantity: int,
                 reason: str,
                 handled_by: int):
        self.order_id = order_id
        self.return_date = return_date
        self.product_id = product_id
        self.quantity = quantity
        self.reason = reason
        self.handled_by = handled_by


JSONResponse = Union[Response, Tuple[Response, int]]