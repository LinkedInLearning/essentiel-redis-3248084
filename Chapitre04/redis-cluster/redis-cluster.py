import redis

r = redis.RedisCluster(host='localhost', port=6372, charset="utf-8", decode_responses=True)
# r = redis.Redis(host='localhost', port=6372, charset="utf-8", decode_responses=True)

print(r.get_nodes())

mem = r.info("memory")

print(mem["used_memory_human"])