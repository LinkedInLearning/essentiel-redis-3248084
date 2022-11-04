import os
import redis

r = redis.Redis(host='localhost', port=6379, db=0)
fichiers = os.listdir("D:\\")

print(fichiers)

r.delete("fichiers")

for f in fichiers:
    r.rpush("fichiers", f)

print(r.lpop("fichiers").decode('UTF_8'))
