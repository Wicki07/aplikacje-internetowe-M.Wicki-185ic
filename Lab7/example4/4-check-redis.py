from redis import Redis

redis_connection = Redis(decode_responses=True)

redis_connection.sadd("key","value1")
redis_connection.sadd("key","value2")
redis_connection.sadd("key","value3")

print(redis_connection.smembers("key"))