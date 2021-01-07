from timeit import timeit

setup ="""from redis import Redis
from timeit import timeit

redis_connection = Redis(decode_responses=True, db=0)

key = "test"

redis_connection.set(key, 0)
"""

stmt1 ="""
i = 10000
while i >= 0:
    redis_connection.incr(key)
    i -= 1

"""

stmt2 ="""
i = 10000
with redis_connection.pipeline() as pipe:
    while i >= 0:
        pipe.incr(key)
        i -= 1
    pipe.execute()
"""

print(timeit(stmt1, setup=setup, number=10))
print(timeit(stmt2, setup=setup, number=10))