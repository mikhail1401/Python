import redis

with redis.Redis() as redis_client:
    value = redis_client.rpop("queue")  # rpop убирает элемент справа (FirstInFirstOut)

print(int(value))