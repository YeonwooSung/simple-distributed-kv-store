import redis


class RedisConnection:
    def __init__(self, host):
        self.host = host
        self.pool = redis.ConnectionPool.from_url(f"redis://{host}")

    def get_conn(self):
        return redis.StrictRedis(connection_pool=self.pool)

    def reconnect(self):
        self.pool.disconnect()
        self.pool = redis.ConnectionPool.from_url(f"redis://{self.host}")
        return self.get_conn()
