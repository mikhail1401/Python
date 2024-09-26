import redis
import random

# Redis commands:
# ping - to ensure redis is working; should return PONG
# set key 'value' - declares a variable and assigns a value to it
# get key - returns the value of the variable
# keys * - returns all the existing keys
# LRANGE key start stop - retrieves a range of elements from the list (key)

# redis_server = redis.Redis() - создаем соединение с Редис

# Контекстный менеджер with автоматичиски прекращает соединение
# после выполнения комманд внутри
with redis.Redis() as redis_server:
    redis_server.lpush("queue", random.randint(0, 10))   # Закидываем единицу в очередь слева (FirstInFirstOut)
