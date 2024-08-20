import redis
from pony.orm import db_session
from ..Category.Category_Repository import CategoryRepository
from ..Unit.Unit_Repository import UnitRepository
from ..Product.Product_Repository import ProductRepository
from .Redis_Client import RedisClient


class PreloadData:
    def __init__(self,
                 redis_client: RedisClient,
                 category_repository: CategoryRepository,
                 unit_repository: UnitRepository,
                 product_repository: ProductRepository
                 ):
        self.redis_client = redis_client
        self.category_repository = category_repository
        self.unit_repository = unit_repository
        self.product_repository = product_repository
        self.load_data()


    @db_session
    def load_data(self):
        for obj in self.category_repository.get_all():
            self.redis_client.set("Categories", obj, str(obj['id']))

        for obj in self.unit_repository.get_all():
            self.redis_client.set("Units", obj, str(obj['id']))

        for obj in self.product_repository.get_all():
            self.redis_client.set("Products", obj, str(obj['id']))
