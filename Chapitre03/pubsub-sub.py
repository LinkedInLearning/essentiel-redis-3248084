import redis

r = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)

sub = r.pubsub()
sub.subscribe('poeme')

for ligne in sub.listen():
    if ligne is not None:
        print(ligne)