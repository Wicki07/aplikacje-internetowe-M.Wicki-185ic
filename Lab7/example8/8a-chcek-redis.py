from redis import Redis

redis_connection = Redis(decode_responses=True, db=0)


script ="""
return {KEYS[1],KEYS[2],ARGV[1],ARGV[2]}
"""

print(redis_connection.eval(script,2,1,2,'first','second'))