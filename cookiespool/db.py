import random
import redis
from cookiespool.config import *


class RedisClient(object):
    def __init__(self, type, website, host=REDIS_HOST, port=REDIS_PORT, passwrod=REDIS_PASSWORD):
        '''
        Redis数据库初始化
        :param type:
        :param website:
        :param host:
        :param port:
        :param passwrod:
        '''
        self.db = redis.StrictRedis(host=host, port=port, password=passwrod, decode_responses=True)
        self.type = type
        self.website = website