from redis import Redis

redis_connection = Redis(decode_responses=True, db=0)

stream_name ='testowy_strumien'

starting_point ="$"

while True:
    message = redis_connection.xread({stream_name: starting_point}, block=10, count=1)
    if message:
        message = message[0][1][0]
        msg_id = message[0]
        msg_payload = message[1]
        starting_point = msg_id
        redis_connection.xdel(stream_name, msg_id)
        print(msg_payload, msg_id)