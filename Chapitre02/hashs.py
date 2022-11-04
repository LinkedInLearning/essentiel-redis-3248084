import redis

r = redis.Redis(host='localhost', port=6379, db=0)

user = r.hgetall('user:01')

print(user)

print(f'cet utilisateur est {user[b"profession"].decode("UTF-8")}')

for cle, valeur in user.items():
    print(cle.decode('UTF-8'), ':', valeur.decode('UTF-8'))