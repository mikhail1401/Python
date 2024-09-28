import redis

with redis.Redis() as redis_client:
    value = redis_client.rpop("queue")  # rpop removes and reutrns value on the right (FirstInFirstOut)

print(int(value))

# with redis.Redis() as redis_client:
#     value = redis_client.brpop("queue")  # brpop waits for a new value if the list is empty

# print(int(value[1]))  # value[0] will be the array's name in this case