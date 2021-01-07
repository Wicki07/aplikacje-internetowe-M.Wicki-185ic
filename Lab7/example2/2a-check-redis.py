from redis import Redis

redis_connection = Redis()

key ="key1"
value ="value1"

redis_connection.set(key, value)
print(redis_connection.get(key))