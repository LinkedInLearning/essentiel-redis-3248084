docker pull redis
docker images

docker run --name redis01 -d redis
docker exec -it redis01 /bin/bash

# commande complète
docker run --name redis01 -d -p 6379:6379 -v d:\redis_data:/var/lib/redis redis redis-server /var/lib/redis/redis.conf