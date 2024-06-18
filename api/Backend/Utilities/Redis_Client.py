import redis
from ..Config.index import Config
import json


class RedisClient:
    def __init__(self):
        self.config = Config()
        self.client = redis.StrictRedis(host=self.config.redis_host, port=self.config.redis_port, db=0)

    def set(self, key, value, id):
        self.client.hset(key, id, json.dumps(value))

    def get(self, key, id):
        value = self.client.hget(key, str(id))
        if value:
            return json.loads(value)
        return None

    def get_all(self, key):
        all_categories_serialized = self.client.hgetall(key)
        return {k.decode('utf-8'): json.loads(v) for k, v in all_categories_serialized.items()}

    def delete(self, key, id):
        self.client.hdel(key, id)
