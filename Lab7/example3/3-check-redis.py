from redis import Redis

redis_connection = Redis(decode_responses=True)

list_key ="przykladowa-lista"

redis_connection.rpush(list_key,1,2,3,4,5)

print(redis_connection.lrange(list_key,0, -1))