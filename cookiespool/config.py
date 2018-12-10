# Redis配置
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = 'None'

# 使用的浏览器
BROWSER_TYPE = 'Chrome'
GENERATOR_MAP = {
    'weibo': 'WeiboCookiesGenerator'
}
# 产生器和验证器循环周期
CYCLE = 120
# 产生器开关，模拟登录添加Cookies
GENERATOR_PROCESS = False
# 验证器开关，循环检测数据库中Cookies是否可用，不可用删除
VALID_PROCESS = False
# API接口服务
API_PROCESS = True