from redis import Redis

redis_connection = Redis(decode_responses=True, db=0)

permission ='ADD_BOOKING'

redis_connection.sadd("users_group:2", *list(range(0,50)))

redis_connection.sadd('permissions', permission)


add_permission_script ="""
local is_valid_permission = redis.call('sismember', 'permissions', KEYS[2])
if is_valid_permission == 1 then
    local users = redis.call('smembers','users_group:'..KEYS[1])
    for _, user in ipairs(users) do
        redis.call('sadd', 'user_permissions:'..user, KEYS[2])
    end
    return true
else
    return false
end
"""


sha= redis_connection.script_load(add_permission_script)
print(redis_connection.evalsha(sha,2,2, permission))