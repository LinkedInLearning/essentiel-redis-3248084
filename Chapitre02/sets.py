import uuid
import redis
from datetime import datetime, time

r = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)

cle = datetime.now().strftime("%Y-%m-%dT%H:%M")
user = str(uuid.uuid4())
print(user)

pipe = r.pipeline(transaction=False)
pipe.sadd(cle, user)

for i in range(20000):
	id = str(uuid.uuid4())
	if i % 100 == 0:
		pipe.sadd(user, id)
	pipe.sadd(cle, id)

pipe.execute()
