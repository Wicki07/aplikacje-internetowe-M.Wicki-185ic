from redis import Redis

redis_connection = Redis(decode_responses=True)

redis_connection.set("key","value")

redis_connection_1 = Redis(decode_responses=True, db=1)

print(redis_connection_1.get("key"))

print(redis_connection.get("key"))