import redis
from ..Config.index import Config
import json
from datetime import datetime
import logging


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)


def datetime_decoder(dct):
    for key, value in dct.items():
        try:
            dct[key] = datetime.fromisoformat(value)
        except (TypeError, ValueError):
            pass
    return dct


class RedisClient:
    def __init__(self):
        self.config = Config()
        self.client = redis.StrictRedis(host=self.config.redis_host, port=self.config.redis_port, db=0)

    def set(self, key, value, item_id):
        self.client.hset(key, str(item_id), json.dumps(value, cls=DateTimeEncoder))

    def get_by_id(self, key, item_id):
        value = self.client.hget(key, str(item_id))
        if value:
            return json.loads(value, object_hook=datetime_decoder)
        return None

    def get_all(self, key):
        all_categories_serialized = self.client.hgetall(key)
        categories_dict = {k.decode('utf-8'): json.loads(v, object_hook=datetime_decoder) for k, v in
                           all_categories_serialized.items()}
        return list(categories_dict.values())

    def delete(self, key, item_id):
        self.client.hdel(key, item_id)
