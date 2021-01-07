from redis import Redis

redis_connection = Redis(decode_responses=True) 

key ="key2b"
value ="value2b"

redis_connection.set(key, value)
print(redis_connection.get(key))