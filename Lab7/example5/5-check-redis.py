from redis import Redis

redis_connection = Redis(decode_responses=True)

pubsub = redis_connection.pubsub()
pubsub.subscribe("testowa_kanal_komunikacyjny")

for message in pubsub.listen():
    print(message)