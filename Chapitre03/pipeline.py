import uuid
import redis
from datetime import datetime

r = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)

cle = datetime.now().strftime("%Y-%m-%dT%H:%M")

pipe = r.pipeline()

for i in range(20000):
	id = str(uuid.uuid4())
	pipe.sadd(cle, id)

pipe.execute()
print("fini")
