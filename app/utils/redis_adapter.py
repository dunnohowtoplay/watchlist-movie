try:
    import ujson as json
except ImportError:
    import json

from redis import Redis
from redis.exceptions import RedisError
from app.config import settings


class RedisAdapter:
    def __init__(self, redis_connection_params, prefix):
        self._redis_connection = Redis(**redis_connection_params)
        self.prefix = prefix

    def exists(self, key):
        key = f'{self.prefix}:{key}'

        try:
            result = self._redis_connection.exists(key)
        except RedisError:
            return False

        return result

    def get(self, key, serializer=json):
        key = f'{self.prefix}:{key}'

        try:
            value = self._redis_connection.get(key)
        except RedisError:
            return None

        return serializer.loads(value)

    def set(self, key, value, timeout=None, serializer=json):
        key = f'{self.prefix}:{key}'

        if timeout is None:
            timeout = settings.REDIS_DEFAULT_TIMEOUT
        value = serializer.dumps(value)
        try:
            self._redis_connection.setex(key, timeout, value)
        except RedisError:
            return False

        return True

    def invalidate(self, key):
        key = f'{self.prefix}:{key}'

        try:
            keys = self._redis_connection.keys(key)
            for k in keys:
                self._redis_connection.delete(k)
        except RedisError:
            return False

        return True
