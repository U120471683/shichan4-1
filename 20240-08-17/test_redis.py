import os
import redis

# 從環境變量中獲取 Redis 連接 URL
redis_url = os.environ['RENDER_REDIS']

# 創建 Redis 連接
render_redis_conn = redis.Redis.from_url(redis_url)

# 測試連接
try:
    render_redis_conn.ping()
    print("Redis 連接成功！")
except redis.ConnectionError:
    print("Redis 連接失敗！")
