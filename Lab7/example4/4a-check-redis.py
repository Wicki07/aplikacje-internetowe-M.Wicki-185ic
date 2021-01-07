from redis import Redis

redis_connection = Redis(decode_responses=True)

redis_connection.zadd("sortowanie",{"key1": 1})
redis_connection.zadd("sortowanie",{"key2": 1})
redis_connection.zadd("sortowanie",{"key3": 1})
redis_connection.zadd("sortowanie",{"key4": 1})

print(redis_connection.zrange("sortowanie",0, -1, withscores = True))