from redis import Redis

redis_connection = Redis(decode_responses=True)

hash_key ='testowy-hash'

redis_connection.hset(hash_key,'key','value')