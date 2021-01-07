from redis import Redis

redis_connection = Redis(decode_responses=True, db=0)

stream_name ='testowy_strumien'

redis_connection.xadd(stream_name,{'testowy_klucz': 'testowa_wartosc'})
message = redis_connection.xread({stream_name: '0-0'}, block=None, count=1)

print(message)