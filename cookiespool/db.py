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

    def name(self):
        '''
        获取Hash的名称
        :return:
        '''
        return "{type}:{website}".format(type=self.type, website=self.website)

    def set(self, username, value):
        '''
        设置键值对
        :param username: 用户名
        :param value: 密码或Cookies
        :return:
        '''
        return self.db.hset(self.name(), username, value)

    def get(self, username):
        '''
        根据键名获取键值
        :param username: 用户名
        :return:
        '''
        return self.db.hget(self.name(), username)